<template>
    <span class="icon-text">
        <span class="icon">
            <i class="fa-solid fa-user fa-2xl"></i>
        </span>
        <span class="ml-5"><b>{{ userName }}</b></span>
    </span>

    <div class="control mt-4">
        <div style="display: flex; align-items: center;">
            <vue3-star-ratings 
                v-model="this.rating"
                starSize="16"
                starColor="#ff9800"
                inactiveColor="#333333"
                controlBg="#2e5090"
                controlColor="#ffffff" 
                controlSize="24" 
                :numberOfStars="5"
                :step="0.5"
                :showControl="false" 
                :disableClick="true" 
            />
            <span class="ml-2">{{ this.rating }}</span>
        </div>
    </div>

    <div class="control mt-4 mb-6">
        {{ text }}
    </div>
</template>

<script>
    import vue3StarRatings from "vue3-star-ratings";
    export default {
        name: 'Review',
        props: ['userName', 'rating', 'text'],
        components: {
            vue3StarRatings
        },
        data () {
            return {
            }
        }
}
</script>
