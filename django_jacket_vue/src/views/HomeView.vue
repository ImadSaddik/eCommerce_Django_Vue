<template>
  <div class="home">
    <section class="hero is-medium is-dark mb-6">
      <div class="hero-body has-text-centered">
        <p class="title mb-6">
          Welcome to Djacket
        </p>
        <p class="subtitle">
          The best jacket store online
        </p>
      </div>
    </section>

    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">Latest products</h2>
      </div>

      <ProductBox
        v-for="product in latestProducts"
        v-bind:key="product.id"
        v-bind:product="product"
      />
    </div>
  </div>
</template>

<script>
  import axios from 'axios'
  import { toast } from 'bulma-toast'
  import ProductBox from '@/components/ProductBox.vue'

  export default {
    name: 'HomeView',
    data() {
      return {
        latestProducts: []
      }
    },
    components: {
      ProductBox
    },
    mounted() {
      this.getLatestProducts();
      document.title = 'Home | Djackets'
    },
    methods: {
      async getLatestProducts() {
        this.$store.commit('setIsLoading', true)

        await axios
          .get('/api/v1/latest-products/')
          .then(response => {
            this.latestProducts = response.data;
          })
          .catch(error => {
            toast({
              message: 'Something went wrong. Please try again!',
              type: 'is-danger',
              dismissible: true,
              pauseOnHover: true,
              duration: 2000,
              position: 'bottom-right',
            })
          })

        this.$store.commit('setIsLoading', false)
      }
    }
  }
</script>
