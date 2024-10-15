<template>
  <Nav/>

  <v-container class="pt-10">
    <v-row justify="center">
      <v-col cols="6" xl="4">
        <v-responsive>
          <v-carousel height="600" width="600" hide-delimiters progress>
            <v-carousel-item>
              <v-img
                :src="listingDetails.photo"
                class="carousel-image"
              ></v-img>
            </v-carousel-item>
            <v-carousel-item>
              <v-img
                src="@/assets/dress2.jpeg"
                class="carousel-image"
              ></v-img>
            </v-carousel-item>
            <v-carousel-item>
              <v-img
                src="@/assets/dress3.jpeg"
                class="carousel-image"
              ></v-img>
            </v-carousel-item>
            <v-carousel-item>
              <v-img
                src="@/assets/museum.jpeg"
                class="carousel-image"
              ></v-img>
            </v-carousel-item>
          </v-carousel>
        </v-responsive>
      </v-col>

      <v-col cols="6" xl="4">
        <v-card>
          <v-btn
            :icon="isHearted ? 'mdi-heart' : 'mdi-heart-outline'"
            @click="toggleHeart"
            class="ml-4 mt-4"
          ></v-btn>
          <v-card-title>
            <h1>{{ listingDetails.title }}
              <v-btn
                v-if="isCurrentUser"
                icon="mdi-account-edit"
                class="ml-2"
                variant="outlined"
                style="color: lightgrey;"
              ></v-btn>
            </h1>
          </v-card-title>
          <v-card-subtitle>
            <h2>{{ listingDetails.price }} €</h2>
          </v-card-subtitle>
          <v-card-text>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam non urna orci. Nulla facilisi. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam non urna orci. Nulla facilisi. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam non urna orci. Nulla facilisi.</p>
            <br>
            <p>Suspendisse potenti. Duis vehicula orci nec dolor fermentum, ut feugiat turpis congue.</p>
          </v-card-text>
        </v-card>
        <v-spacer class="my-4"></v-spacer>
        <v-card
          @click="goToseller(seller.id)"
        >
          <v-card-subtitle class="mt-4">
            <h2>About the seller</h2>
          </v-card-subtitle>
          <v-card-text>
            <v-row justify="center">
              <v-col cols="2" class="d-flex justify-center align-center">
                <v-avatar size="70">
                  <v-img
                    :src="seller.profile_picture"
                  ></v-img>
                </v-avatar>
                
              </v-col>
              <v-col>
                <h1>{{ seller.username }}</h1>
                <div>
                  <v-icon>mdi-star</v-icon>
                  <v-icon>mdi-star</v-icon>
                  <v-icon>mdi-star</v-icon>
                  <v-icon>mdi-star-half-full</v-icon>
                  <v-icon>mdi-star-outline</v-icon>
                </div>
              </v-col>
            </v-row>
          </v-card-text>
        </v-card>

        <v-spacer class="my-8"></v-spacer>

        <v-btn
          block
          color="rgb(199, 189, 231)"
          rounded
          class="pa-4"
          @click="createOrder()"
        >
          Buy now
        </v-btn>

        <v-spacer class="my-4"></v-spacer>

        <v-btn
          block
          variant="outlined"
          color="rgb(199, 189, 231)"
          rounded
          class="pa-4"
        >
          Ask a question
        </v-btn>
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
  import axios from 'axios';

  import Nav from '@/components/Nav.vue'

  export default {
    data() {
      return {
        currentUser: null,
        isCurrentUser: false,
        listingId: null,
        listingDetails: [],
        seller: [],
        isHearted: false
      };
    },
    created() {
      this.listingId = this.$route.params.id;
      this.getCurrentUser();
    },
    methods: {
      fetchListingDetails(listingId) {
        axios.get(`http://localhost:8000/shop/api/listings/${listingId}`)
            .then(response => {
                this.listingDetails = response.data;
                this.seller = this.listingDetails.user;

                if (this.currentUser.active_login) {
                  this.isCurrentUser = (this.seller.username == this.currentUser.username);
                }
            
                console.log(`Current user? ${this.isCurrentUser}`)
            })
            .catch(error => {
                console.error('Error fetching listing details:', error);
            });
      },
      toggleHeart() {
        this.isHearted = !this.isHearted;
      },
      goToseller(userId) {
        this.$router.push(`/users/${userId}/profile`);
      },
      createOrder() {
        this.$router.push(`/order/create`);
      },
      getCurrentUser() {
          axios.get('http://localhost:8000/shop/api/users/current-user')
            .then(response => {
                this.currentUser = response.data;
                this.fetchListingDetails(this.listingId);
            })
            .catch(error => {
                console.error(`Error fetching current user: ${error}`);
            });
      }
    }
  };

</script>