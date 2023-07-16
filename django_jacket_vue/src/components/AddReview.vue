<template>
    <div class="column is-9">
        <h1 class="title is-4"><b>Add review</b></h1>

        <div class="notification is-danger mt-4" v-if="errors.length">
            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
        </div>

        <textarea class="textarea" placeholder="Write your review." v-model="text"></textarea>
        <div class="control mt-4">
            <div style="display: flex; align-items: center;">
                <h1 class="mr-5">Rate this product</h1>
                <vue3-star-ratings 
                    v-model="rating"
                    starSize="24"
                    starColor="#ff9800"
                    inactiveColor="#333333"
                    controlBg="#2e5090"
                    controlColor="#ffffff" 
                    controlSize="24" 
                    :numberOfStars="5"
                    :step="0.5"
                    :showControl="true" 
                    :disableClick="true" 
                />
                <span class="ml-2">{{ rating }} stars</span>
            </div>
        </div> 

        <div class="column mt-4">
            <a class="button is-dark is-pulled-right" @click="addReview">Add review</a>
        </div>
    </div>
</template>

<script>
    import axios from "axios";
    import vue3StarRatings from "vue3-star-ratings";

    export default {
        name: 'AddReview',
        props: ['product'],
        components: {
            vue3StarRatings
        },
        data () {
            return {
                rating: 0,
                text: '',
                errors: []
            }
        },
        methods: {
            async addReview() {
                this.$store.commit('setIsLoading', true)

                const data = {
                    product: this.product.id,
                    user: 0,
                    text: this.text,
                    rating: this.rating,
                };

                if (this.text === '') {
                    this.errors.push('Text is required.');
                    return;
                } else {
                    this.errors = [];
                }

                await axios
                    .post('/api/v1/sendReview/', data)
                    .then(response => {
                        this.clearTextAreaAndRating();
                        this.$emit('reviewAdded', this.product.id);
                    })
                    .catch(error => {
                        console.log("Error");
                    })

                this.$store.commit('setIsLoading', false)
            },
            clearTextAreaAndRating() {
                this.text = '';
            }
        }
    }
</script>
