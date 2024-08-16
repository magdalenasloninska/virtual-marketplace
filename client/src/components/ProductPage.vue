<template>
  <Nav/>

  <v-container class="pt-10">
    <v-row justify="center">
      <v-col cols="12" md="6">
        <v-responsive>
          <v-carousel height="600" width="600" hide-delimiters progress>
            <v-carousel-item>
              <v-img
                src="@/assets/dress.jpeg"
                class="carousel-image"
              ></v-img>
            </v-carousel-item>
            <v-carousel-item>
              <v-img
                src="../assets/dress2.jpeg"
                class="carousel-image"
              ></v-img>
            </v-carousel-item>
            <v-carousel-item>
              <v-img
                src="../assets/dress3.jpeg"
                class="carousel-image"
              ></v-img>
            </v-carousel-item>
            <v-carousel-item>
              <v-img
                src="../assets/museum.jpeg"
                class="carousel-image"
              ></v-img>
            </v-carousel-item>
          </v-carousel>
        </v-responsive>
      </v-col>

      <v-col cols="12" md="6">
        <v-card>
          <v-btn
            :icon="isHearted ? 'mdi-heart' : 'mdi-heart-outline'"
            @click="toggleHeart"
            class="pa-4"
          ></v-btn>
          <v-card-title>
            <h1>Tie-dye dress</h1>
          </v-card-title>
          <v-card-subtitle>
            <h2>129 €</h2>
          </v-card-subtitle>
          <v-card-text>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam non urna orci. Nulla facilisi. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam non urna orci. Nulla facilisi. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam non urna orci. Nulla facilisi.</p>
            <br>
            <p>Suspendisse potenti. Duis vehicula orci nec dolor fermentum, ut feugiat turpis congue.</p>
          </v-card-text>
        </v-card>
        <v-spacer class="my-8"></v-spacer>
        <v-btn block color="rgb(199, 189, 231)" rounded class="pa-4">Buy now</v-btn>
        <v-spacer class="my-4"></v-spacer>
        <v-btn block variant="outlined" color="rgb(199, 189, 231)" rounded class="pa-4">Ask a question</v-btn>
      </v-col>
    </v-row>
  </v-container>

</template>

<style scoped>
  .carousel-image {
    object-fit: contain;
    max-width: 100%;
    max-height: 100%;
    width: auto;
    height: auto;
    display: block;
    margin: auto;
  }

  .image-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100%;
    width: 100%;
  }
</style>

<script>
  import Nav from './Nav.vue'

  export default {
    data() {
      return {
        isHearted: false
      };
    },
    methods: {
      toggleHeart() {
        this.isHearted = !this.isHearted;
      }
    }
  };
</script>