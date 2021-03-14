<template>
  <nav
    class="navbar is-white has-shadow"
    role="navigation"
    aria-label="main navigation"
  >
    <div class="navbar-brand">
      <router-link class="navbar-item" to="/">
        <h1 class="title">Sales App</h1>
      </router-link>

      <a
        role="button"
        class="navbar-burger"
        aria-label="menu"
        aria-expanded="false"
        @click="toggleNavbar"
      >
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
      </a>
    </div>

    <div class="navbar-menu" ref="menu">
      <div class="mt-2 navbar-start">
        <router-link class="navbar-item" to="/">Home</router-link>
        <router-link class="navbar-item" to="/about">About</router-link>
      </div>

      <div v-if="is_logged" class="navbar-end">
        <router-link class="navbar-item" to="/cart"
          >Shopping Cart ( {{ cart }} )</router-link
        >
        <div class="dropdown is-right navbar-item" ref="account">
          <div class="dropdown-trigger">
            <button
              @click="toggleAccount"
              class="button"
              style="border: none"
              aria-haspopup="true"
              aria-controls="dropdown-menu"
            >
              <span>Account</span>
              <span class="icon is-small">
                <i class="fas fa-angle-down" aria-hidden="true"></i>
              </span>
            </button>
          </div>
          <div class="dropdown-menu" id="dropdown-menu" role="menu">
            <div class="dropdown-content">
              <div class="dropdown-item">
                <p>
                  {{ user.email }}
                </p>
              </div>
              <hr class="dropdown-divider" />
              <router-link class="dropdown-item" to="/orders"
                >Orders</router-link
              >
              <a @click="logout" class="dropdown-item">Logout</a>
            </div>
          </div>
        </div>
      </div>
      <div v-else class="navbar-end">
        <router-link class="navbar-item" to="/login">Login</router-link>
        <router-link class="navbar-item" to="/register">Register</router-link>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'Header',
  data() {
    return {
      is_logged: Boolean,
      user: Object,
      cart: Number
    };
  },
  methods: {
    toggleNavbar() {
      this.$refs.menu.classList.toggle('is-active');
    },
    toggleAccount() {
      this.$refs.account.classList.toggle('is-active');
    },
    logout() {
      localStorage.removeItem('token');
      if (this.$route.name == 'Home') location.reload();
      else this.$router.push({ name: 'Home' });
    }
  },
  async mounted() {
    try {
      const cart = localStorage.getItem('cart');
      if (cart != null) this.cart = JSON.parse(cart).length;
      else this.cart = 0;
      const options = {
        headers: { Authorization: localStorage.getItem('token') }
      };
      const resp = await fetch(`${process.env.VUE_APP_SALES}/users`, options);
      if (resp.status == 400) {
        this.is_logged = false;
        if (this.$route.name == 'cart' || this.$route.name == 'Orders') {
          this.$router.push('/');
        }
        throw 'Not Authorized';
      } else {
        const data = await resp.json();
        if (data == 'Not Authorized') {
          this.is_logged = false;
          if (this.$route.name == 'Cart' || this.$route.name == 'Orders') {
            this.$router.push('/');
          }
        } else {
          this.is_logged = true;
          this.user = data;
        }
      }
    } catch (err) {
      console.log(err);
    }
  }
};
</script>
