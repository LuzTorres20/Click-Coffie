document.addEventListener('DOMContentLoaded', function() {
    var productos = document.querySelectorAll('.producto');

    productos.forEach(function(producto) {
        var disminuir = producto.querySelector('.disminuir');
        var aumentar = producto.querySelector('.aumentar');
        var cantidadSpan = producto.querySelector('.cantidad');
        var cantidadInput = producto.querySelector('.cantidad-input');

        var count = 1;

        disminuir.addEventListener('click', function() {
            if(count > 1) {
                count--;
                cantidadSpan.textContent = count;
                cantidadInput.value = count;
                console.log('Cantidad actual:', count); // <-- Línea de prueba
            }
        });

        aumentar.addEventListener('click', function() {
            count++;
            cantidadSpan.textContent = count;
            cantidadInput.value = count;
            console.log('Cantidad actual:', count); // <-- Línea de prueba
        });
    });
});
