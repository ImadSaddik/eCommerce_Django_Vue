<template>
    <div class="page-product">
        <div class="columns is-multiline">
            <div class="column is-9">
                <figure class="image mb-6">
                    <img v-bind:src="product.get_image">
                </figure>

                <h1 class="title">{{ product.name }}</h1>
                <p>{{ product.description }}</p>
            </div>

            <div class="column is-3">
                <h2 class="subtitle">Information</h2>
                <p><strong>Price: </strong>${{ product.price }}</p>
                
                <div class="field has-addons mt-6">
                    <div class="control">
                        <input type="number" class="input" min="1" v-model="quantity">
                    </div>

                    <div class="control">
                        <a class="button is-dark" @click="addToCart">Add to cart</a>
                    </div>
                </div>
            </div>
        </div>
        
        <AddReview 
            :product="product"
            @review-added="refreshPage"
        />

        <div class="column is-9 mt-4">
            <h1 class="title is-4"><b>Other reviews</b></h1>
            <Review 
                v-for="review in reviews"
                :userName="review.user"
                :rating="review.rating"
                :text="review.text"
            />
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import  { toast } from 'bulma-toast';
import Review from '@/components/Review.vue';
import AddReview from '@/components/AddReview.vue';

export default {
    name: 'ProductView',
    components: {
        Review,
        AddReview
    },
    data() {
        return {
            quantity: 1,
            product: {},
            reviews: [],
        }
    },
    mounted() {
        this.getProduct();
    },
    methods: {
        async getProduct() {
            this.$store.commit('setIsLoading', true)
            const category_slug = this.$route.params.category_slug
            const product_slug = this.$route.params.product_slug

            await axios
                .get(`/api/v1/products/${category_slug}/${product_slug}`)
                .then(response => {
                    this.product = response.data;
                    document.title = this.product.name + ' | Djackets'
                    this.getReviews(this.product.id);
                })
                .catch(error => {
                    toast({
                        message: 'Something went wrong. Please try again',
                        type: 'is-danger',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'bottom-right',
                    })
                })

            this.$store.commit('setIsLoading', false)
        },
        async getReviews(product_id) {
            await axios
                .get(`/api/v1/reviews/${product_id}`)
                .then(response => {
                    this.reviews = response.data;
                })
                .catch(error => {
                    toast({
                        message: 'Something went wrong. Please try again',
                        type: 'is-danger',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'bottom-right',
                    })
                })

            this.$store.commit('setIsLoading', false)
        },
        addToCart() {
            if (isNaN(this.quantity) || this.quantity <= 0) {
                this.quantity = 1
            }

            const item = {
                product: this.product,
                quantity: this.quantity
            }

            this.$store.commit('addToCart', item)

            toast({
                message: 'The product was added to the cart',
                type: 'is-success',
                dismissible: true,
                pauseOnHover: true,
                duration: 2000,
                position: 'bottom-right',
            })
        },
        refreshPage(product_id) {
            this.$router.back();
            this.$router.forward();
        }
    }
}
</script>
