import streamlit as st


class AFD:
    def __init__(self):
        # Define los estados del AFD
        self.states =   [
                            "q0", "q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9", "q10", 
                            "q11", "q12", "q13", "q14", "q15", "q16", "q17","q18","q19","q20","q21",
                            "q22","q23","q24","q25","q26","q27","q28","q29","q30","q31","q32","q33","q34","q35","q36","q37","q38","39","40","41","42","43"
                        ]
        
        # Define el estado inicial
        self.initial_state = "q1"
        
        # Define los estados finales
        self.final_states = ["q5","q10","q18","q24","q27","q33"]
        
        # Define las transiciones del AFD
        self.transitions = {
           
            #cadenas 
         
            ("q1", "5"): "q19",
            ("q1", "7"): "q2",
            ("q1", "P"): "q11",
            ("q1", "3"): "q34",

            ("q2", "P"): "q3",
            ("q3", "R"): "q4",
            ("q4", "O"): "q5",
            
            ("q5", "5"): "q6",
            ("q5", "6"): "q28",
            
            ("q6", "6"): "q40",
            ("q6", "8"): "q7",
            ("q7", "5"): "q8",
        
            ("q8", "0"): "q9",
            ("q9", "U"): "q10",
            
            
            ("q11", "R"): "q12",
            
            ("q12", "O"): "q13",
            ("q13", "6"): "q29",
            ("q13", "7"): "q14",
            ("q14", "6"): "q15",
            
            ("q15", "0"): "q16",
            ("q16", "0"): "q17",            
            ("q17", "0"): "q18",

            ("q19", "0"): "q25",
            ("q19", "5"): "q20",
            ("q19", "P"): "q41",
            
            
            ("q20", "6"): "q21",
            ("q21", "0"): "q22",
        
            ("q22", "0"): "q23",
            ("q23", "U"): "q24",
            
            ("q25", "0"): "q26",
            ("q26", "0"): "q27",
            ("q28", "8"): "q7",
            
            ("q29", "0"): "q30",
            ("q30", "0"): "q31",
            
            ("q31", "0"): "q32",
            
            
            
            ("q32", "U"): "q33",
            
            ("q34", "P"): "q35",
            ("q35", "R"): "q36",
            
            ("q36", "O"): "q37",
            ("q37", "5"): "q38",
            ("q38", "4"): "q39",
            ("q39", "5"): "q8",
            ("q40", "5"): "q8",
            ("q41", "R"): "q42",
            ("q42", "O"): "q43",
            ("q43", "5"): "q6",
            
            
           
        }
        
    def accepts(self, word):
        # Establece el estado actual 
        current_state = self.initial_state
        
        # Lista para almacenar los estados visitados
        estados_visitados = [current_state]
        
        # Lista para almacenar las transiciones con el formato 'q1->q2'
        transiciones = []
        
        # Recorre cada símbolo de la palabra
        for symbol in word:
            # Obtiene el estado de destino mediante la transición
            next_state = self.transitions.get((current_state, symbol))
            
            # Si no hay transición, la palabra no es aceptada
            if next_state is None:
                return False, transiciones, estados_visitados
            
            # Agrega la transición a la lista
            transiciones.append(f'{current_state}->{next_state}')
            
            # Actualiza el estado actual
            current_state = next_state
            
            # Agrega el estado actual a la lista de estados visitados
            estados_visitados.append(current_state)
        
        # Si el estado actual es un estado final, la palabra es aceptada
        if current_state in self.final_states:
            return True, transiciones, estados_visitados
        else:
            return False, transiciones, estados_visitados


afd = AFD()

st.header('Automata')
st.subheader('Ingrese una cadena para validar')

cadena = st.text_input("Cadena")

if st.button('Validar'):
    validacion, transiciones, estados_visitados = afd.accepts(cadena)
    if validacion:
        st.write('La cadena es: Verdadero')
        st.write('Transiciones: ' + ' -> '.join(transiciones))
        st.write('Estados Visitados:', ' -> '.join(estados_visitados))
    else:
        st.write('La cadena es: Falso')