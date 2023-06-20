const add_card = document.querySelector(".add_card");
const footer = document.querySelector("footer");

add_card.addEventListener("click", () => {
  footer.innerHTML = `
  <div class="menu_agregar_producto">
  <form action="agregar_producto/" method="post">
    {% csrf_token %}
    <div>
      <h2>Agregar producto</h2>
      <div>clave del producto {{form.clave_producto}}</div>
      <div>nombre del producto {{form.nombre_producto}}</div>
    </div>
  </form>
</div>
  `;
});
console.log(add_card);
