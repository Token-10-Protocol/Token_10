#!/usr/bin/env python3
"""
Sistema Automático de Evaluación para Acceso al Núcleo IZA - OPTIMIZADO
"""

import json
from datetime import datetime, timedelta
import math
from functools import lru_cache

class EvaluadorAccesoIZA:
    def __init__(self, ruta_formulario_base=None):
        self.umbrales = {
            'LECTOR_VERIFICADO': 70,
            'COLABORADOR_AVANZADO': 85,
            'INVESTIGADOR_NUCLEAR': 95
        }
        
        self.pesos = {
            'contribuciones': 0.40,
            'conocimiento': 0.30,
            'compromiso': 0.30
        }
        
        # Cache para formulario base
        self._ruta_formulario_base = ruta_formulario_base
        self._formulario_cache = None
    
    def cargar_formulario(self, ruta_formulario):
        """Carga el formulario con cache básico"""
        if ruta_formulario == self._ruta_formulario_base and self._formulario_cache:
            return self._formulario_cache
            
        with open(ruta_formulario, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        if ruta_formulario == self._ruta_formulario_base:
            self._formulario_cache = data
            
        return data
    
    def evaluar_solicitud(self, formulario):
        """Evalúa completa la solicitud de acceso - OPTIMIZADA"""
        # Cachear tiempo de evaluación para consistencia
        tiempo_evaluacion = datetime.now()
        
        # Calcular puntajes individuales
        puntaje_contribuciones = self._calcular_puntaje_contribuciones_opt(formulario['seccion_contribuciones'])
        puntaje_conocimiento = self._calcular_puntaje_conocimiento_opt(formulario['seccion_conocimiento'])
        puntaje_compromiso = self._calcular_puntaje_compromiso_opt(formulario['seccion_compromiso'])
        
        # Puntaje ponderado total
        puntaje_total = (
            puntaje_contribuciones * self.pesos['contribuciones'] +
            puntaje_conocimiento * self.pesos['conocimiento'] + 
            puntaje_compromiso * self.pesos['compromiso']
        )
        
        # Determinar nivel recomendado
        tiempo_participacion = self._calcular_tiempo_participacion_opt(
            formulario['solicitante']['fecha_ingreso_comunidad'],
            tiempo_evaluacion
        )
        
        nivel_recomendado = self._determinar_nivel(puntaje_total, tiempo_participacion)
        
        return {
            'puntaje_total': round(puntaje_total, 2),
            'nivel_recomendado': nivel_recomendado,
            'desglose': {
                'contribuciones': puntaje_contribuciones,
                'conocimiento': puntaje_conocimiento,
                'compromiso': puntaje_compromiso
            },
            'tiempo_participacion_dias': tiempo_participacion,
            'fecha_evaluacion': tiempo_evaluacion.isoformat()
        }
    
    def _calcular_puntaje_contribuciones_opt(self, contribuciones):
        """Versión optimizada - reduce llamadas a min()"""
        # Pre-calcular todos los valores primero
        calculos = [
            ('commits_aceptados', 5, 25),
            ('issues_resueltos', 4, 20),
            ('discusiones_significativas', 3, 15),
            ('documentacion_mejorada', 4, 20),
            ('revisiones_pull_requests', 2, 20)
        ]
        
        puntaje = 0
        for clave, multiplicador, maximo in calculos:
            valor = contribuciones.get(clave, 0)  # Más seguro que acceso directo
            puntaje += min(valor * multiplicador, maximo)
        
        return min(puntaje, 100)
    
    def _calcular_puntaje_conocimiento_opt(self, conocimiento):
        """Versión optimizada - evita cálculos repetidos"""
        # Lista de factores predefinida
        factores = {
            'mano_cosmica': 4,
            'tres_ciclos': 4,
            'operadores_iza': 4,
            'matematica_avanzada': 3,
            'protocolos_basicos': 3
        }
        
        # Suma más eficiente
        puntaje_base = sum(
            conocimiento.get(clave, 0) * factor 
            for clave, factor in factores.items()
        )
        
        # Optimizar: calcular longitud una sola vez
        explicacion = conocimiento.get('explicacion_comprension', '').strip()
        longitud = len(explicacion)
        
        if longitud > 100:
            puntaje_base += 10
        elif longitud > 50:
            puntaje_base += 5
            
        return min(puntaje_base, 100)
    
    def _calcular_puntaje_compromiso_opt(self, compromiso):
        """Versión optimizada - reduce duplicación de código"""
        puntaje = 0
        
        # Compromisos éticos (más robusto con .get())
        if compromiso.get('acepta_principios_iza', False):
            puntaje += 15
        if compromiso.get('compromiso_no_comercial', False):
            puntaje += 15
            
        # Disponibilidad de tiempo
        horas = compromiso.get('disponibilidad_horas_semana', 0)
        if horas >= 10:
            puntaje += 40
        elif horas >= 5:
            puntaje += 25
        elif horas >= 2:
            puntaje += 15
            
        # Calidad de motivación (optimizado)
        motivacion = compromiso.get('motivacion_participacion', '').strip()
        longitud = len(motivacion)
        
        if longitud > 200:
            puntaje += 30
        elif longitud > 100:
            puntaje += 20
        elif longitud > 50:
            puntaje += 10
            
        return min(puntaje, 100)
    
    def _calcular_tiempo_participacion_opt(self, fecha_ingreso, tiempo_referencia):
        """Optimizado: usa tiempo de referencia en lugar de now() cada vez"""
        if not fecha_ingreso:
            return 0
            
        fecha_ingreso_dt = datetime.fromisoformat(fecha_ingreso)
        return (tiempo_referencia - fecha_ingreso_dt).days
    
    # Mantener función original para compatibilidad
    def _calcular_tiempo_participacion(self, fecha_ingreso):
        return self._calcular_tiempo_participacion_opt(fecha_ingreso, datetime.now())
    
    def _determinar_nivel(self, puntaje, dias_participacion):
        """Misma lógica pero más legible"""
        if (puntaje >= self.umbrales['INVESTIGADOR_NUCLEAR'] and 
            dias_participacion >= 365):
            return "INVESTIGADOR_NUCLEAR"
        elif (puntaje >= self.umbrales['COLABORADOR_AVANZADO'] and 
              dias_participacion >= 180):
            return "COLABORADOR_AVANZADO"
        elif (puntaje >= self.umbrales['LECTOR_VERIFICADO'] and 
              dias_participacion >= 90):
            return "LECTOR_VERIFICADO"
        else:
            return "ACCESO_DENEGADO"

    # Método adicional para evaluación por lotes
    def evaluar_lote_solicitudes(self, lista_formularios):
        """Optimizado para múltiples evaluaciones"""
        tiempo_base = datetime.now()
        resultados = []
        
        for formulario in lista_formularios:
            # Reutilizar tiempo base para consistencia
            resultado = self.evaluar_solicitud(formulario)
            resultados.append(resultado)
            
        return resultados

# Cache para instancias del evaluador (si se usa múltiples veces)
@lru_cache(maxsize=1)
def obtener_evaluador():
    return EvaluadorAccesoIZA()

# Ejemplo de uso optimizado
if __name__ == "__main__":
    # Usar evaluador cacheado
    evaluador = obtener_evaluador()
    
    # Cargar formulario de ejemplo (con cache si es el base)
    formulario = evaluador.cargar_formulario('formulario-evaluacion.json')
    
    # Evaluar solicitud
    resultado = evaluador.evaluar_solicitud(formulario)
    
    print("=== RESULTADO DE EVALUACIÓN OPTIMIZADA ===")
    print(f"Puntaje Total: {resultado['puntaje_total']}/100")
    print(f"Nivel Recomendado: {resultado['nivel_recomendado']}")
    print(f"Tiempo Participación: {resultado['tiempo_participacion_dias']} días")
    print("\nDesglose:")
    for categoria, puntaje in resultado['desglose'].items():
        print(f"  {categoria.capitalize()}: {puntaje}/100")
