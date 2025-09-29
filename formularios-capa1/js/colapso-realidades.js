// formularios-capa1/js/colapso-realidades.js
// 🎯 SISTEMA DE COLAPSO DE REALIDADES - CAPA 1
// ✨ MEJORA: Añadido feedback de visión antes de redirección

document.addEventListener('DOMContentLoaded', function() {
    const colapsoForm = document.getElementById('colapsoForm');
    const visionInput = document.getElementById('visionInput');
    const contadorCaracteres = document.getElementById('contadorCaracteres');
    
    // Contador de caracteres en tiempo real
    visionInput.addEventListener('input', function() {
        const longitud = this.value.length;
        contadorCaracteres.textContent = `${longitud}/10 caracteres mínimos`;
        
        // Cambiar color según longitud
        if (longitud < 10) {
            contadorCaracteres.style.color = '#ff4444';
        } else if (longitud < 20) {
            contadorCaracteres.style.color = '#ffaa00';
        } else {
            contadorCaracteres.style.color = '#00ff88';
        }
    });
    
    // Manejar envío del formulario
    colapsoForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const vision = visionInput.value.trim();
        
        // Validación básica
        if (vision.length < 10) {
            alert('❌ Tu visión necesita al menos 10 caracteres para generar el colapso.');
            return;
        }
        
        // Guardar en localStorage
        localStorage.setItem('visionUsuario', vision);
        localStorage.setItem('fechaColapso', new Date().toISOString());
        
        // Efectos visuales de colapso
        iniciarColapsoVisual(vision);
    });
    
    function iniciarColapsoVisual(vision) {
        const container = document.querySelector('.container');
        const formContainer = document.querySelector('.form-container');
        
        // Efecto de desvanecimiento
        formContainer.style.transition = 'all 1s ease';
        formContainer.style.opacity = '0.3';
        formContainer.style.transform = 'scale(0.95)';
        
        // Crear partículas de colapso
        crearParticulasColapso();
        
        // Mostrar resumen antes de redirigir
        setTimeout(() => {
            mostrarResumenVision(vision);
            
            // Redirigir después de mostrar el resumen
            setTimeout(() => {
                window.location.href = 'onboarding-permisos.html';
            }, 3000); // 3 segundos para leer el resumen
        }, 2000); // 2 segundos para efectos visuales
    }
    
    // 🆕 NUEVA FUNCIÓN: MOSTRAR RESUMEN DE VISIÓN
    function mostrarResumenVision(vision) {
        const formContainer = document.querySelector('.form-container');
        
        const resumen = document.createElement('div');
        resumen.className = 'resumen-vision';
        resumen.innerHTML = `
            <div class="resumen-container">
                <h3>✨ TU VISIÓN HA SIDO REGISTRADA</h3>
                <div class="resumen-stats">
                    <p><strong>📝 Contenido:</strong> "${vision.substring(0, 60)}${vision.length > 60 ? '...' : ''}"</p>
                    <p><strong>📊 Longitud:</strong> ${vision.length} caracteres</p>
                    <p><strong>🔵 Nivel:</strong> Capa 1 - Visión Inicial</p>
                    <p><strong>⏰ Fecha:</strong> ${new Date().toLocaleString()}</p>
                </div>
                <div class="proximo-paso">
                    <p>🔄 Redirigiendo al sistema de permisos...</p>
                </div>
            </div>
        `;
        
        // Añadir estilos inline para el resumen
        resumen.style.cssText = `
            margin: 20px 0;
            animation: fadeInUp 0.8s ease;
        `;
        
        formContainer.appendChild(resumen);
    }
    
    function crearParticulasColapso() {
        const container = document.querySelector('.container');
        const particles = 15;
        
        for (let i = 0; i < particles; i++) {
            const particle = document.createElement('div');
            particle.style.cssText = `
                position: absolute;
                width: 4px;
                height: 4px;
                background: #00ffff;
                border-radius: 50%;
                pointer-events: none;
                animation: particleFloat 1.5s ease-out forwards;
                left: 50%;
                top: 50%;
            `;
            
            // Dirección aleatoria
            const angle = Math.random() * Math.PI * 2;
            const distance = 100 + Math.random() * 100;
            const duration = 1 + Math.random() * 0.5;
            
            particle.style.setProperty('--angle', angle);
            particle.style.setProperty('--distance', distance + 'px');
            particle.style.setProperty('--duration', duration + 's');
            
            container.appendChild(particle);
            
            // Remover después de la animación
            setTimeout(() => {
                particle.remove();
            }, 1500);
        }
    }
});

// Añadir estilos CSS para las animaciones
const style = document.createElement('style');
style.textContent = `
    @keyframes particleFloat {
        0% {
            transform: translate(0, 0) scale(1);
            opacity: 1;
        }
        100% {
            transform: translate(
                calc(cos(var(--angle)) * var(--distance)),
                calc(sin(var(--angle)) * var(--distance))
            ) scale(0);
            opacity: 0;
        }
    }
    
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .resumen-container {
        background: linear-gradient(135deg, 
            rgba(0, 255, 255, 0.1) 0%, 
            rgba(255, 255, 0, 0.1) 100%);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid rgba(0, 255, 255, 0.3);
        backdrop-filter: blur(10px);
    }
    
    .resumen-container h3 {
        color: #00ffff;
        margin-bottom: 15px;
        text-align: center;
        font-size: 1.2em;
    }
    
    .resumen-stats p {
        margin: 8px 0;
        color: #e0e0e0;
        font-size: 0.95em;
    }
    
    .proximo-paso {
        margin-top: 15px;
        padding-top: 15px;
        border-top: 1px solid rgba(0, 255, 255, 0.2);
        text-align: center;
        color: #00ff88;
        font-style: italic;
    }
`;
document.head.appendChild(style);