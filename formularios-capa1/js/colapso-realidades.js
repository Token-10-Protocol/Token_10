document.getElementById('formCapa1').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const vision = document.getElementById('vision-inicial').value;
    const btn = document.querySelector('.btn-colapsar');
    
    if (vision.trim().length < 10) {
        alert('🌱 Tu semilla de realidad necesita más energía. Escribe al menos 10 caracteres.');
        return;
    }
    
    btn.innerHTML = '🌀 COLAPSANDO REALIDAD...';
    btn.style.background = 'var(--amarillo-colapso)';
    btn.style.color = 'var(--negro-vacio)';
    btn.disabled = true;
    
    // Guardar visión y redirigir DIRECTAMENTE al onboarding
    localStorage.setItem('vision-colapsada', vision);
    
    // Redirección directa después de 2 segundos
    setTimeout(() => {
        window.location.href = 'onboarding-permisos.html';
    }, 2000);
});

// Mantener efectos visuales
document.getElementById('vision-inicial').addEventListener('focus', function() {
    this.style.transform = 'scale(1.02)';
});

document.getElementById('vision-inicial').addEventListener('blur', function() {
    this.style.transform = 'scale(1)';
});

document.addEventListener('DOMContentLoaded', function() {
    console.log('🌀 Portal de Colapso de Realidades - Cargado');
});
