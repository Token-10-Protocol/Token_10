#!/usr/bin/env python3
"""
Sistema Automático de Evaluación para Acceso al Núcleo IZA
"""

import json
from datetime import datetime, timedelta
import math

class EvaluadorAccesoIZA:
    def __init__(self):
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
    
    def cargar_formulario(self, ruta_formulario):
        """Carga el formulario de evaluación desde archivo JSON"""
        with open(ruta_formulario, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def evaluar_solicitud(self, formulario):
        """Evalúa completa la solicitud de acceso"""
        
        # Calcular puntajes individuales
        puntaje_contribuciones = self._calcular_puntaje_contribuciones(formulario['seccion_contribuciones'])
        puntaje_conocimiento = self._calcular_puntaje_conocimiento(formulario['seccion_conocimiento'])
        puntaje_compromiso = self._calcular_puntaje_compromiso(formulario['seccion_compromiso'])
        
        # Puntaje ponderado total
        puntaje_total = (
            puntaje_contribuciones * self.pesos['contribuciones'] +
            puntaje_conocimiento * self.pesos['conocimiento'] + 
            puntaje_compromiso * self.pesos['compromiso']
        )
        
        # Determinar nivel recomendado
        tiempo_participacion = self._calcular_tiempo_participacion(formulario['solicitante']['fecha_ingreso_comunidad'])
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
            'fecha_evaluacion': datetime.now().isoformat()
        }
    
    def _calcular_puntaje_contribuciones(self, contribuciones):
        """Calcula puntaje basado en contribuciones a la zona pública"""
        puntaje = 0
        
        # Commits aceptados (máx 25 puntos)
        puntaje += min(contribuciones['commits_aceptados'] * 5, 25)
        
        # Issues resueltos (máx 20 puntos)
        puntaje += min(contribuciones['issues_resueltos'] * 4, 20)
        
        # Discusiones significativas (máx 15 puntos)
        puntaje += min(contribuciones['discusiones_significativas'] * 3, 15)
        
        # Documentación mejorada (máx 20 puntos)
        puntaje += min(contribuciones['documentacion_mejorada'] * 4, 20)
        
        # Revisiones PR (máx 20 puntos)
        puntaje += min(contribuciones['revisiones_pull_requests'] * 2, 20)
        
        return min(puntaje, 100)
    
    def _calcular_puntaje_conocimiento(self, conocimiento):
        """Evalúa el conocimiento teórico de IZA"""
        # Puntaje base por comprensión (1-5 escala)
        puntaje_base = sum([
            conocimiento['mano_cosmica'] * 4,
            conocimiento['tres_ciclos'] * 4,
            conocimiento['operadores_iza'] * 4,
            conocimiento['matematica_avanzada'] * 3,
            conocimiento['protocolos_basicos'] * 3
        ])
        
        # Ajuste por explicación de comprensión
        explicacion = conocimiento['explicacion_comprension']
        if len(explicacion.strip()) > 100:
            puntaje_base += 10
        elif len(explicacion.strip()) > 50:
            puntaje_base += 5
            
        return min(puntaje_base, 100)
    
    def _calcular_puntaje_compromiso(self, compromiso):
        """Evalúa el compromiso ético y disponibilidad"""
        puntaje = 0
        
        # Compromisos éticos (30 puntos)
        if compromiso['acepta_principios_iza']:
            puntaje += 15
        if compromiso['compromiso_no_comercial']:
            puntaje += 15
            
        # Disponibilidad de tiempo (40 puntos)
        horas = compromiso['disponibilidad_horas_semana']
        if horas >= 10:
            puntaje += 40
        elif horas >= 5:
            puntaje += 25
        elif horas >= 2:
            puntaje += 15
            
        # Calidad de motivación (30 puntos)
        motivacion = compromiso['motivacion_participacion']
        if len(motivacion.strip()) > 200:
            puntaje += 30
        elif len(motivacion.strip()) > 100:
            puntaje += 20
        elif len(motivacion.strip()) > 50:
            puntaje += 10
            
        return min(puntaje, 100)
    
    def _calcular_tiempo_participacion(self, fecha_ingreso):
        """Calcula días de participación desde fecha de ingreso"""
        if not fecha_ingreso:
            return 0
            
        fecha_ingreso_dt = datetime.fromisoformat(fecha_ingreso)
        return (datetime.now() - fecha_ingreso_dt).days
    
    def _determinar_nivel(self, puntaje, dias_participacion):
        """Determina el nivel de acceso recomendado"""
        if puntaje >= self.umbrales['INVESTIGADOR_NUCLEAR'] and dias_participacion >= 365:
            return "INVESTIGADOR_NUCLEAR"
        elif puntaje >= self.umbrales['COLABORADOR_AVANZADO'] and dias_participacion >= 180:
            return "COLABORADOR_AVANZADO"
        elif puntaje >= self.umbrales['LECTOR_VERIFICADO'] and dias_participacion >= 90:
            return "LECTOR_VERIFICADO"
        else:
            return "ACCESO_DENEGADO"

# Ejemplo de uso
if __name__ == "__main__":
    evaluador = EvaluadorAccesoIZA()
    
    # Cargar formulario de ejemplo
    formulario = evaluador.cargar_formulario('formulario-evaluacion.json')
    
    # Evaluar solicitud
    resultado = evaluador.evaluar_solicitud(formulario)
    
    print("=== RESULTADO DE EVALUACIÓN ===")
    print(f"Puntaje Total: {resultado['puntaje_total']}/100")
    print(f"Nivel Recomendado: {resultado['nivel_recomendado']}")
    print(f"Tiempo Participación: {resultado['tiempo_participacion_dias']} días")
    print("\nDesglose:")
    for categoria, puntaje in resultado['desglose'].items():
        print(f"  {categoria.capitalize()}: {puntaje}/100")
