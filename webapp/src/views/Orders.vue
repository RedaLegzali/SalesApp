<template>
  <Header />
  <div class="container mt-5">
    <div v-if="orders.length > 0">
      <div v-for="order in orders" :key="order.id" class="box">
        <div class="block">
          <span class="tag is-light is-medium">Order: {{ order._id }}</span>
        </div>
        <table class="table">
          <thead>
            <tr>
              <th>Sku</th>
              <th>Price $</th>
              <th>Quantity</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="sku in order.skus" :key="sku.id">
              <td>{{ sku.name }}</td>
              <td>{{ sku.price }}</td>
              <td>{{ sku.quantity }}</td>
            </tr>
          </tbody>
        </table>
        <div class="block">
          <span class="tag is-light is-medium">Total: {{ order.price }} $</span>
        </div>
      </div>
    </div>
    <div v-else>
      <h1 class="subtitle">You have no orders yet</h1>
    </div>
  </div>
</template>

<script>
import Header from '@/components/Header.vue';

export default {
  name: 'Orders',
  components: {
    Header
  },
  data() {
    return {
      orders: Array
    };
  },
  async mounted() {
    const options = {
      method: 'GET',
      headers: {
        Authorization: localStorage.getItem('token')
      }
    };
    const resp = await fetch(`${process.env.VUE_APP_SALES}/orders`, options);
    const data = await resp.json();
    this.orders = data;
  }
};
</script>
