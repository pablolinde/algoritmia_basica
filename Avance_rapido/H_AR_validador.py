import numpy as np

def validador_H_AR(fichero_entrada, fichero_salida, fichero_salida_profesor=None):
    
    """
    Función que valida el algoritmo implementado.
    Parámetros:
        * fichero_entrada: ruta al fichero con los datos de entrada con los que se ha alimentado el algoritmo propuesto.
        * fichero_salida: ruta al fichero con los resultados generados por el algoritmo propuesto.
        * fichero_salida_profesor: ruta al fichero con los resultados de prueba.
    """
    
    file_salida= open(fichero_salida)
    
    file_salida_prof= None
    if fichero_salida_profesor is not None:
        file_salida_prof= open(fichero_salida_profesor)

    with open(fichero_entrada) as file:
        num_pruebas= int(file.readline())
        
        for i in range(num_pruebas):
            
            N,M = [int(number) for number in file.readline().strip().split(' ')]  
            
            mat_= []
            for j in range(0,N):
                a = [int(number) for number in file.readline().strip().split(' ')]  
                mat_.append(a)

            tiempos_ejecucion= np.vstack(mat_)  
            
            #print(N,M,tiempos_ejecucion)
            
            procesamiento_acumulado= int(file_salida.readline())
            orden_seleccion= [int(number) for number in file_salida.readline().strip().split(' ')]
            maquina_ejecucion= [int(number) for number in file_salida.readline().strip().split(' ')]
            
            procesamiento_acumulado_prof= None
            if file_salida_prof:
                procesamiento_acumulado_prof= int(file_salida_prof.readline())
                file_salida_prof.readline()
                file_salida_prof.readline()               

            if len(orden_seleccion) != len(set(orden_seleccion)):
                print(f"ERROR en el caso {i}: En el orden de selección se encuentran tareas asignadas más de una vez al procesador.")
            else:
                procesamiento_acumulado_calculado=np.zeros(M)
                for j in range(N):
                    p= orden_seleccion[j]
                    m= maquina_ejecucion[j]
                    procesamiento_acumulado_calculado[m-1] += tiempos_ejecucion[p-1,m-1]
                
                procesamiento_acumulado_calculado_max= max(procesamiento_acumulado_calculado)
                if procesamiento_acumulado != procesamiento_acumulado_calculado_max:
                    print(f"ERROR en el caso {i}: el procesamiento acumulado para la máquina con mayor carga no se ha calculado correctamente. Procesamiento acumulado indicado: {procesamiento_acumulado}. Procesamiento acumulado  correcto: {procesamiento_acumulado_calculado_max}")
                elif (procesamiento_acumulado_prof is not None) and (procesamiento_acumulado_calculado_max > (procesamiento_acumulado_prof * 3)):
                    print(f"ERROR en el caso {i}: el procesamiento acumulado para la máquina es mayor al tripe de la solucion proporcionada por el profesor. Procesamiento acumulado para la máquina en la solucion: {procesamiento_acumulado_calculado_max}. Peso total ahorrado por el profesor: {procesamiento_acumulado_prof}")       
                else:
                    print(f"Todo correcto para el caso {i}.")   

#Ejemplo de aplicación                    
validador_H_AR('./tests/T2/703b.in', './tests/T2/test1703b.out', './tests/T2/703b.out')