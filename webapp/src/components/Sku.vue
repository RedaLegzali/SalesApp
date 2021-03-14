<template>
  <div class="card mt-5">
    <div class="card-image">
      <figure class="image">
        <img :src="require(`@/assets/images/skus/${image}`)" :alt="name" />
      </figure>
    </div>
    <div class="card-content">
      <div class="media">
        <div class="media-content">
          <p class="subtitle">{{ name }}</p>
        </div>
      </div>

      <div
        class="content flex is-flex-direction-row is-justify-content-space-between"
      >
        <div v-if="price == original" class="price mt-2 mb-2">
          <p>{{ price }} $</p>
        </div>
        <div v-else class="price">
          <s>{{ original }} $</s>
          <p>{{ price }} $</p>
        </div>
        <div v-if="quantity > 0" class="stock">
          <p class="has-text-primary">In Stock ( {{ quantity }} )</p>
          <input
            class="button is-rounded pr-2"
            type="number"
            ref="quantity"
            value="1"
            min="1"
            :max="quantity"
          />
          <button
            @click="cart"
            ref="button"
            class="button is-rounded is-info"
            style="float: right"
          >
            Add to Cart
          </button>
        </div>
        <div v-else class="stock">
          <p class="has-text-danger">Out of Stock</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Sku',
  props: {
    id: Number,
    name: String,
    original: Number,
    quantity: Number,
    price: Number,
    image: String
  },
  methods: {
    cart() {
      const quantity = this.$refs.quantity.value;
      let cart = localStorage.getItem('cart');
      if (cart == null) {
        cart = [
          {
            id: this.id,
            name: this.name,
            quantity: quantity,
            price: this.price
          }
        ];
        localStorage.setItem('cart', JSON.stringify(cart));
      } else {
        let exists = false;
        const button = this.$refs.button;
        cart = JSON.parse(cart);
        cart.forEach(element => {
          if (element.name == this.name) {
            element.quantity = quantity;
            exists = true;
          }
        });
        if (!exists) {
          cart.push({
            id: this.id,
            name: this.name,
            quantity: quantity,
            price: this.price
          });
        }
        localStorage.setItem('cart', JSON.stringify(cart));
        button.innerHTML = 'Added !';
        button.classList.remove('is-info');
        button.classList.add('is-primary');
        setTimeout(function() {
          button.innerHTML = 'Add to cart';
          button.classList.remove('is-primary');
          button.classList.add('is-info');
        }, 3000);
      }
    }
  }
};
</script>

<style scoped>
img {
  width: 300px;
  height: 300px;
}
.card {
  width: 300px;
}
</style>
