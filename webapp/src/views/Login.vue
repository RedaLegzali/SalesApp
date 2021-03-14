<template>
  <Header />
  <div class="container mt-5">
    <article class="message is-danger">
      <div class="message-header">
        <p>Failure</p>
      </div>
      <div class="message-body"></div>
    </article>
    <form @submit.prevent="submit">
      <div class="field">
        <label class="label">Email</label>
        <div class="control has-icons-left has-icons-right">
          <input
            class="input"
            type="email"
            id="email"
            placeholder="Email"
            v-model="email"
          />
          <span class="icon is-small is-left">
            <i class="fas fa-envelope"></i>
          </span>
        </div>
      </div>

      <div class="field">
        <label class="label">Password</label>
        <div class="control has-icons-left has-icons-right">
          <input
            class="input"
            type="password"
            id="password"
            placeholder="Password"
            v-model="password"
          />
          <span class="icon is-small is-left">
            <i class="fas fa-key"></i>
          </span>
        </div>
      </div>

      <div class="field is-grouped">
        <div class="control">
          <button class="button is-link">Submit</button>
        </div>
        <div class="control">
          <button @click="back" class="button is-link is-light">Cancel</button>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
import Header from '@/components/Header.vue';

export default {
  name: 'Login',
  components: {
    Header
  },
  data() {
    return {
      email: '',
      password: ''
    };
  },
  methods: {
    submit() {
      const is_empty = string => {
        return string.length == 0 ? true : false;
      };
      const is_email = string => {
        let pattern = /^[\w\W]+@\w+\.\w+$/;
        return pattern.test(string);
      };
      const email = document.querySelector('#email');
      const password = document.querySelector('#password');
      let validation = true;
      let message = '';
      if (is_empty(this.email) || !is_email(this.email)) {
        email.classList.remove('is-success');
        email.classList.add('is-danger');
        validation = false;
        message += '<p>Email is empty or invalid</p>';
      } else {
        email.classList.remove('is-danger');
        email.classList.add('is-success');
      }
      if (is_empty(this.password)) {
        password.classList.remove('is-success');
        password.classList.add('is-danger');
        validation = false;
        message += '<p>Password is empty</p>';
      } else {
        password.classList.remove('is-danger');
        password.classList.add('is-success');
      }
      if (validation) {
        const data = {
          email: this.email,
          password: this.password
        };
        const options = {
          method: 'POST',
          headers: {
            Accept: 'application/json',
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(data)
        };
        fetch(`${process.env.VUE_APP_SALES}/users/login`, options)
          .then(resp => {
            if (resp.status == 400) {
              throw 'Incorrect Email or Password';
            } else {
              return resp.json();
            }
          })
          .then(data => {
            document.querySelector('.message-header').childNodes[0].innerHTML =
              'Success';
            document.querySelector('.message').classList.remove('is-danger');
            document.querySelector('.message').classList.add('is-success');
            document.querySelector('.message-body').innerHTML =
              'You are connected ! You will be redirected';
            document.querySelector('.message').style.display = 'block';
            localStorage.setItem('token', 'Bearer ' + data['accessToken']);
            const redirect = () => {
              this.$router.push('/');
            };
            setTimeout(function() {
              redirect();
            }, 2000);
          })
          .catch(err => {
            document.querySelector('.message-body').innerHTML = err;
            document.querySelector('.message').style.display = 'block';
          });
      } else {
        document.querySelector('.message').style.display = 'block';
        document.querySelector('.message-body').innerHTML = message;
      }
    }
  }
};
</script>

<style scoped>
.field {
  margin-bottom: 20px;
  margin-top: 20px;
}
.message {
  display: none;
}
</style>
