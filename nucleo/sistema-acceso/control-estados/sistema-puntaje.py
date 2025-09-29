# nucleo/sistema-acceso/control-estados/sistema-puntaje.py
"""
SISTEMA DE PUNTAJE EVOLUCIONADO - ENFOQUE OPTIMIZACIÓN CUÁNTICA
Evalúa solicitudes basado en OPTIMIZACIÓN de recursos, no solo méritos
"""

def evaluar_solicitud_optimizada(datos_solicitud):
    """
    NUEVO ENFOQUE: Evalúa basado en OPTIMIZACIÓN de recursos
    en lugar de solo méritos individuales
    """
    
    puntuacion = {
        "colaboracion_vectorial": 0.0,    # ¿Cómo optimiza el ecosistema?
        "innovacion_tecnica": 0.0,        # Calidad técnica
        "optimizacion_recursos": 0.0,     # Eficiencia energética (NUEVO)
        "viabilidad_real": 0.0,           # Factibilidad real
        "puntaje_total": 0.0
    }
    
    # CALCULAR CADA DIMENSIÓN
    puntuacion["colaboracion_vectorial"] = calcular_aportes_ecosistema(datos_solicitud)
    puntuacion["innovacion_tecnica"] = calcular_calidad_tecnica_mejorada(datos_solicitud)
    puntuacion["optimizacion_recursos"] = calcular_eficiencia_recursos(datos_solicitud)
    puntuacion["viabilidad_real"] = calcular_viabilidad_mejorada(datos_solicitud)
    
    # NUEVA fórmula con enfoque optimización
    puntuacion["puntaje_total"] = (
        puntuacion["colaboracion_vectorial"] * 0.35 +    # Más peso a colaboración
        puntuacion["optimizacion_recursos"] * 0.30 +     # Importante: eficiencia
        puntuacion["innovacion_tecnica"] * 0.20 +
        puntuacion["viabilidad_real"] * 0.15
    )
    
    return puntuacion

def calcular_aportes_ecosistema(datos):
    """
    Evalúa CÓMO OPTIMIZA el ecosistema completo
    """
    puntaje = 0.0
    
    if datos.get("fortalece_ecosistema"):
        puntaje += 0.3
    
    if datos.get("comparte_conocimiento"):
        puntaje += 0.3
        
    # NUEVO: Evalúa optimización colectiva
    if datos.get("optimizacion_colectiva"):
        nivel_optimizacion = datos["optimizacion_colectiva"]
        if nivel_optimizacion == "alta":
            puntaje += 0.4
        elif nivel_optimizacion == "media":
            puntaje += 0.2
    
    return min(puntaje, 1.0)

def calcular_eficiencia_recursos(datos):
    """
    NUEVA FUNCIÓN: Evalúa optimización de recursos
    """
    puntaje = 0.0
    
    # Métricas de eficiencia energética
    if datos.get("reduccion_consumo"):
        reduccion = datos["reduccion_consumo"]
        if reduccion >= 0.5:    # 50% o más de reducción
            puntaje += 0.4
        elif reduccion >= 0.3:  # 30-49% de reducción
            puntaje += 0.2
    
    # Eficiencia de infraestructura
    if datos.get("ahorro_infraestructura"):
        ahorro = datos["ahorro_infraestructura"]
        if ahorro == "significativo":
            puntaje += 0.3
        elif ahorro == "moderado":
            puntaje += 0.15
    
    # Sostenibilidad a largo plazo
    if datos.get("sostenibilidad_largo_plazo"):
        if datos["sostenibilidad_largo_plazo"] == "alta":
            puntaje += 0.3
    
    return min(puntaje, 1.0)

def calcular_calidad_tecnica_mejorada(datos):
    """
    Mantiene lógica original pero añade criterios de optimización
    """
    puntaje = 0.0
    
    if datos.get("nivel_tecnico") == "avanzado":
        puntaje += 0.4
    elif datos.get("nivel_tecnico") == "intermedio":
        puntaje += 0.2
    
    # NUEVO: Evalúa eficiencia del código/arquitectura
    if datos.get("eficiencia_tecnica"):
        if datos["eficiencia_tecnica"] == "alta":
            puntaje += 0.3
        elif datos["eficiencia_tecnica"] == "media":
            puntaje += 0.15
    
    # Calidad técnica base
    if datos.get("buenas_practicas"):
        puntaje += 0.3
    
    return min(puntaje, 1.0)

def calcular_viabilidad_mejorada(datos):
    """
    EVOLUCIÓN: Ahora considera viabilidad de OPTIMIZACIÓN
    """
    puntaje = 0.0
    
    if datos.get("recursos_suficientes"):
        puntaje += 0.4
    
    if datos.get("tiempo_realista"):
        puntaje += 0.3
    
    # NUEVO: Viabilidad de las métricas de optimización
    if datos.get("metricas_optimizacion_medibles"):
        puntaje += 0.3
    
    return min(puntaje, 1.0)

def decidir_acceso_basado_optimizacion(puntuacion):
    """
    Toma decisión de acceso basado en OPTIMIZACIÓN no solo mérito
    """
    if puntuacion["puntaje_total"] >= 0.8:
        return {
            "acceso": "🔴 ROJO_VECTORIAL",
            "motivo": "Alta optimización de recursos y colaboración vectorial",
            "nivel_confianza": "alto"
        }
    elif puntuacion["puntaje_total"] >= 0.6:
        return {
            "acceso": "🟡 AMARILLO_COLAPSO", 
            "motivo": "Buena optimización, acceso gradual recomendado",
            "nivel_confianza": "medio"
        }
    else:
        return {
            "acceso": "🔵 AZUL_ELECTRICO",
            "motivo": "Necesita demostrar más optimización de recursos",
            "nivel_confianza": "bajo"
        }

# FUNCIÓN DE PRUEBA PARA VERIFICAR
def probar_sistema():
    """
    Prueba el sistema con un ejemplo real
    """
    solicitud_ejemplo = {
        "fortalece_ecosistema": True,
        "comparte_conocimiento": True,
        "optimizacion_colectiva": "alta",
        "reduccion_consumo": 0.6,  # 60% de reducción
        "ahorro_infraestructura": "significativo",
        "sostenibilidad_largo_plazo": "alta",
        "nivel_tecnico": "avanzado",
        "eficiencia_tecnica": "alta",
        "buenas_practicas": True,
        "recursos_suficientes": True,
        "tiempo_realista": True,
        "metricas_optimizacion_medibles": True
    }
    
    print("🔧 PROBANDO SISTEMA DE PUNTAJE OPTIMIZADO...")
    resultado = evaluar_solicitud_optimizada(solicitud_ejemplo)
    decision = decidir_acceso_basado_optimizacion(resultado)
    
    print("📊 PUNTUACIÓN OBTENIDA:")
    for dimension, valor in resultado.items():
        print(f"   {dimension}: {valor:.2f}")
    
    print("\n🎯 DECISIÓN DE ACCESO:")
    print(f"   Nivel: {decision['acceso']}")
    print(f"   Motivo: {decision['motivo']}")
    print(f"   Confianza: {decision['nivel_confianza']}")
    
    return resultado, decision

if __name__ == "__main__":
    probar_sistema()