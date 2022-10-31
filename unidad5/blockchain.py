from hashlib import sha256
import json
import time

'''
Las transacciones se empaquetan en bloques en lotes y un bloque
puede contener una o más transacciones. Los bloques que contienen
transacciones se generan y agregan regularmente a la cadena de bloques.
Debido a que hay muchos bloques, cada bloque debe tener una identificación única.
'''


class Block:
    def __init__(self, index, transactions, timestamp, previuos_hash, nonce=0):
        """
        Constructor para la clase `Block`.
        :param index:         ID único del bloque.
        :param transactions:  Lista de transacciones.
        :param timestamp:     Hora de generación del bloque.
        :param previous_hash: Hash del bloque anterior en la cadena de la que forma parte este bloque.
        :param nonce: El valor de nonce en este punto es nuestra prueba de carga de trabajo.
        """
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previuos_hash
        self.nonce = nonce

    '''
    La función hash puede convertir cualquier tamaño de datos de entrada en datos de salida de tamaño fijo,
    que es el hash de los datos, y diferentes datos de entrada (básicamente) obtendrán diferentes datos de
    salida, por lo que puede usar el hash de salida como entrada La identidad de los datos. Una función hash
    ideal tiene las siguientes características:

        - Debería ser fácil de calcular
        - Debe ser determinista, generar siempre el mismo hash para los mismos datos de entrada
        - Debe tener una aleatoriedad uniforme, un pequeño cambio en los datos de entrada también
          provocará un cambio significativo en el hash de salida

    De esta forma podemos garantizar:

        - Es básicamente imposible adivinar cuáles son los datos de entrada del hash, la única
          forma es probar todas las combinaciones posibles
        - Si conoce la entrada y la salida al mismo tiempo, puede verificar que el hash sea correcto
          simplemente recalculando

    Guardaremos el hash del bloque como un campo del bloque y lo usaremos como una huella digital
    o firma de los datos del bloque.
    '''

    def compute_hash(self):
        """
        Devuelve el hash de la instancia del bloque convirtiendolo primero en una cadena JSON.
        """
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()


'''
Blockchain es una colección de bloques y podemos usar listas de Python
para guardar todos los bloques. Pero esto no es suficiente, porque si
alguien reemplaza deliberadamente un nuevo bloque en la colección con
un bloque anterior, los datos serán alterados.

Necesitamos una forma de asegurarnos de que los cambios en los bloques
anteriores invaliden toda la cadena de bloques. El método utilizado por
Bitcoin es hacer que el hash del bloque siguiente dependa del bloque
anterior. Para vincular los bloques, necesitamos agregar un nuevo campo
en la estructura del bloque para guardar el hash del bloque anterior:
previous_hash.

Bueno, si cada bloque está vinculado al bloque anterior a través del
campo previous_hash, ¿qué pasa con el primer bloque? En el campo de
la cadena de bloques, el primer bloque se llama Genesis Block, que se
puede generar manualmente o usar alguna lógica específica. Ahora
agreguemos el campo previous_hash a la clase Block e implementemos
la definición de la estructura blockchain.

Ahora, si se modifica algún bloque anterior, entonces:

    - El hash del bloque anterior cambiará
    - Esto provocará una inconsistencia con el contenido registrado en
      el campo previous_hash del siguiente bloque
    - Dado que los datos de entrada para calcular el hash del bloque
      contienen el contenido del campo previous_hash, el hash del siguiente
      bloque también cambiará
'''


class Blockchain:
    difficulty = 2  # dificultad del algoritmo PoW

    def __init__(self):
        """
        Constructor para la clase Blockchain
        """
        self.chain = []
        self.unconfirmed_transactions = []
        self.create_genesis_block()

    def create_genesis_block(self):
        """
        Una función para generar un bloque de génesis y lo agrega a
        la cadena. El bloque tiene índice 0, anterior_hash como 0 y
        un hash válido.
        """
        genesis_block = Block(0, [], time.time(), '0')
        genesis_block.hash = self.proof_of_work(genesis_block)
        self.chain.append(genesis_block)

    @property
    def last_block(self):
        """
        Una forma rápida de recuperar el bloque más reciente de la cadena. Tenga en cuenta que
        a cadena siempre constará de al menos un bloque (es decir, bloque de génesis)
        """
        return self.chain[-1]

    '''
    Existe un problema más. Si modificamos el bloque anterior, y si es muy fácil recalcular 
    otros bloques, entonces no es difícil manipular el blockchain. Para evitar este problema, 
    podemos utilizar la mencionada asimetría de la función hash para aumentar la dificultad y 
    aleatoriedad del cálculo del hash del bloque. Lo que tenemos que hacer es: aceptar solo 
    hashes de bloque que cumplan con ciertas restricciones. Ahora agreguemos una restricción 
    que requiere al menos n ceros al comienzo del bloque hash, donde n es un número entero positivo.
    '''

    def proof_of_work(self, block):
        """
        Funcion que prueba diferentes valores del nonce para obtener un hash
        que satisfaga nuestros criterios de dificultad
        """
        block.nonce = 0
        print("Nonce inicial:", block.nonce)
        computed_hash = block.compute_hash()
        while not computed_hash.startswith('0' * Blockchain.difficulty):
            block.nonce += 1
            computed_hash = block.compute_hash()
        print("Nonce final:", block.nonce)
        return computed_hash

    '''
    El proceso anterior es una versión simplificada del algoritmo hashcash utilizado por Bitcoin. 
    El número de ceros a la izquierda especificado en las restricciones determina la dificultad de 
    nuestro algoritmo de prueba de trabajo: cuantos más ceros a la izquierda, más difícil es 
    encontrar un nonce adecuado.

    Al mismo tiempo, debido a la asimetría de la función hash, la prueba de trabajo no es fácil 
    de calcular, pero sí de verificar.

    Cabe señalar que no existe una lógica simple para encontrar rápidamente el valor nonce que 
    satisfaga las restricciones, por lo que solo se pueden realizar cálculos de fuerza bruta.
    '''

    def is_valid_proof(self, block, block_hash):
        """
        Comprueba si block_hash es un hash de bloque valido y cumple los criterios de dificultad
        """
        return (block_hash.startswith('0' * Blockchain.difficulty) and block_hash == block.compute_hash())

    '''
    Para agregar un bloque a la cadena de bloques, primero debemos verificar:

        - Los datos del bloque no han sido alterados y la prueba de trabajo proporcionada 
          es correcta.
        - El orden de las transacciones es correcto y el campo previous_hash apunta al 
          hash del último bloque de nuestra cadena.
    '''

    def add_block(self, block, proof):
        """
        Una función que agrega el bloque a la cadena después de la verificación.
        La verificación incluye:
        * Comprobación de si la prueba es válida.
        * El anterior_hash referido en el bloque y el hash de un último bloque
          en el partido de la cadena.
        """
        previos_hash = self.last_block.hash

        if previos_hash != block.previous_hash:
            return False

        if not self.is_valid_proof(block, proof):
            return False

        block.hash = proof
        self.chain.append(block)
        return True

    '''
    Las transacciones se almacenan inicialmente en el grupo de transacciones no confirmadas. 
    El proceso de poner transacciones no confirmadas en bloques y calcular la prueba de 
    trabajo se conoce como minería. Una vez que se encuentra el nonce que cumple con las 
    restricciones especificadas, podemos decir que se ha excavado un bloque que se puede 
    encadenar.

    En la mayoría de las criptomonedas digitales, incluido Bitcoin, los mineros recibirán 
    recompensas en criptomonedas a cambio de la potencia informática invertida en la prueba 
    de trabajo.
    '''

    def add_new_transaction(self, transaction):
        self.unconfirmed_transactions.append(transaction)

    def mine(self):
        """
        Esta función sirve como interfaz para agregar los pendientes
        transacciones a la cadena de bloques agregándolas al bloque
        y averiguar la prueba de trabajo.
        """

        if not self.unconfirmed_transactions:
            return False

        last_block = self.last_block

        new_block = Block(index=last_block.index+1,
                          transactions=self.unconfirmed_transactions,
                          timestamp=time.time(),
                          previuos_hash=last_block.hash)

        proof = self.proof_of_work(new_block)
        print("Minando")
        print("previous_hash:", last_block.hash)
        print("proof:", proof)

        self.add_block(block=new_block, proof=proof)
        self.unconfirmed_transactions = []
        return new_block.index

    def check_chain_validity(self, chain):
        """
        Un método auxiliar para verificar si toda la cadena de bloques es válida.          
        """
        result = True
        previos_hash = '0'

        # Iterar a traves de toda la cadena
        for block in chain:
            block_hash = block.hash
            # Eliminar el campo hash para volver a calcular el hash nuevamente
            delattr(block, "hash")
            print(block.previous_hash)

            if not self.is_valid_proof(block, block_hash) or previos_hash != block.previous_hash:
                result = False
                break

            block.hash, previos_hash = block_hash, block_hash

        return result
