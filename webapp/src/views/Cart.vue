<template>
  <Header />
  <div class="container mt-5">
    <div v-if="skus.length > 0">
      <table class="table">
        <thead>
          <tr>
            <th>Sku</th>
            <th>Price $</th>
            <th>Quantity</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="sku in skus" :key="sku.id">
            <td>{{ sku.name }}</td>
            <td>{{ sku.price }}</td>
            <td>{{ sku.quantity }}</td>
          </tr>
        </tbody>
      </table>
      <div class="block">
        <span class="tag is-light is-medium">Total: {{ price }} $</span>
      </div>
      <button @click="submit" class="button is-primary is-rounded mr-5">
        Confirm Order
      </button>
      <button @click="erase" class="button is-danger is-rounded">
        Erase Cart
      </button>
    </div>
    <div v-else>
      <h1 class="subtitle">Your shopping cart is empty</h1>
    </div>
  </div>
</template>

<script>
import Header from '@/components/Header.vue';

export default {
  name: 'Cart',
  components: {
    Header
  },
  data() {
    return {
      skus: Array,
      price: 0
    };
  },
  mounted() {
    this.skus = JSON.parse(localStorage.getItem('cart'));
    if (this.skus == null) this.skus = [];
    else {
      this.skus.forEach(element => {
        this.price += element.price;
      });
    }
  },
  methods: {
    submit() {
      const data = {
        skus: this.skus,
        price: this.price
      };
      const options = {
        method: 'POST',
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json',
          Authorization: localStorage.getItem('token')
        },
        body: JSON.stringify(data)
      };
      fetch(`${process.env.VUE_APP_SALES}/orders`, options)
        .then(resp => resp)
        .then(() => {
          localStorage.removeItem('cart');
          this.$router.push('/orders');
        })
        .catch(err => console.log(err));
    },
    erase() {
      localStorage.removeItem('cart');
      location.reload();
    }
  }
};
</script>
