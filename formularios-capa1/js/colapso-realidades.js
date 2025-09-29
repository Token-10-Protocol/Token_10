document.getElementById('formCapa1').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const vision = document.getElementById('vision-inicial').value;
    const btn = document.querySelector('.btn-colapsar');
    
    // Validación básica
    if (vision.trim().length < 10) {
        alert('🌱 Tu semilla de realidad necesita más energía. Escribe al menos 10 caracteres.');
        return;
    }
    
    // Efecto visual de colapso
    btn.innerHTML = '🌀 COLAPSANDO REALIDAD...';
    btn.style.background = 'var(--amarillo-colapso)';
    btn.style.color = 'var(--negro-vacio)';
    btn.disabled = true;
    
    // Simular procesamiento
    setTimeout(() => {
        // Aquí iría la lógica real de envío al backend
        console.log('Visión registrada:', vision);
        
        // Mensaje épico de éxito
        mostrarMensajeExito(vision);
        
    }, 2000);
});

function mostrarMensajeExito(vision) {
    const mensaje = `✨ **REALIDAD COLAPSADA CON ÉXITO** ✨

🌌 Tu visión ha sido registrada en el ecosistema:
"${vision}"

🚀 **Próximos pasos:**
• Prepárate para el onboarding contextual
• Recibirás acceso a la Capa 2 tras tu primera contribución
• Tu semilla influirá en la realidad que construiremos juntos

⚡ **Recuerda:** Eres participe de algo más grande`;

    alert(mensaje);
    
    // Aquí redirigiríamos al onboarding
    // window.location.href = '/onboarding-capa1.html';
    
    // Por ahora resetear el formulario
    setTimeout(() => {
        document.getElementById('formCapa1').reset();
        const btn = document.querySelector('.btn-colapsar');
        btn.innerHTML = '🌌 COLAPSAR ESTA REALIDAD';
        btn.style.background = 'var(--degradado-cosmico)';
        btn.style.color = 'var(--blanco-puro)';
        btn.disabled = false;
    }, 3000);
}

// Efectos adicionales de interactividad
document.getElementById('vision-inicial').addEventListener('focus', function() {
    this.style.transform = 'scale(1.02)';
});

document.getElementById('vision-inicial').addEventListener('blur', function() {
    this.style.transform = 'scale(1)';
});

// Efecto de partículas cósmicas al cargar
document.addEventListener('DOMContentLoaded', function() {
    console.log('🌀 Portal de Colapso de Realidades - Cargado');
    console.log('🌟 Sistema Tricapa Activado');
});
