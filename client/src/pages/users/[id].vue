<template>
  <Nav/>

  <v-container class="pt-10">
    <v-row justify="center">
      <v-col cols="4" xl="3" class="d-flex justify-center">
        <v-avatar size="300">
          <v-img
            :src="userDetails.profile_picture"
          ></v-img>
        </v-avatar>
      </v-col>

      <v-col cols="8" xl="5">
        <v-card>
          <v-card-title>
            <h1>{{ userDetails.username }}</h1>
          </v-card-title>
          <v-card-subtitle>
            <v-icon>mdi-star</v-icon>
            <v-icon>mdi-star</v-icon>
            <v-icon>mdi-star</v-icon>
            <v-icon>mdi-star-half-full</v-icon>
            <v-icon>mdi-star-outline</v-icon>
          </v-card-subtitle>
          <v-spacer class="mb-4"></v-spacer>
          <v-card-subtitle>
            <h2>Joined {{ dateJoined }}</h2>
          </v-card-subtitle>
          <v-card-text>
            <p>{{ userDetails.about }}</p>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>

    <v-spacer class="my-8"></v-spacer>
    <v-row>
      <v-col>
        <div class="d-flex justify-space-between">
          <h3>
            Here you can view {{ userDetails.username }}'s featured listings!
          </h3>
          <v-btn
            append-icon="mdi-arrow-right-bold"
          >
            View all
          </v-btn>
        </div>
        
      </v-col>
    </v-row>
    <v-row>
      <v-col :cols=4>
        <v-hover v-slot="{ isHovering, props }">
          <v-img
            src="@/assets/architecture.jpeg"
            aspect-ratio="1"
            cover
            v-bind="props"
          >
            <v-expand-transition>
              <div
                v-if="isHovering"
                class="d-flex featured text-h3"
              >
                Featured #1
              </div>
            </v-expand-transition>
          </v-img>
        </v-hover>
      </v-col>
      <v-col :cols=4>
        <v-hover v-slot="{ isHovering, props }">
          <v-img
            src="@/assets/dress.jpeg"
            aspect-ratio="1"
            cover
            v-bind="props"
          >
            <v-expand-transition>
              <div
                v-if="isHovering"
                class="d-flex featured text-h3"
              >
                Featured #2
              </div>
            </v-expand-transition>
          </v-img>
        </v-hover>
      </v-col>
      <v-col :cols=4>
        <v-hover v-slot="{ isHovering, props }">
          <v-img
            src="@/assets/museum.jpeg"
            aspect-ratio="1"
            cover
            v-bind="props"
          >
            <v-expand-transition>
              <div
                v-if="isHovering"
                class="d-flex featured text-h3"
              >
                Featured #3
              </div>
            </v-expand-transition>
          </v-img>
        </v-hover>
      </v-col>
    </v-row>
  </v-container>

</template>

<style scoped>
  .featured {
    opacity: .85;
    align-items: center;
    justify-content: center;
    background-color: rgb(81, 69, 118);
    height: 100%;
    font-family: 'Homemade Apple', cursive;
  }
</style>

<script>
  import axios from 'axios';

  import Nav from '@/components/Nav.vue'

  export default {
    data() {
      return {
        userDetails: [],
        dateJoined: null
      };
    },
    created() {
      this.fetchUserDetails(this.$route.params.id)
    },
    methods: {
      fetchUserDetails(userId) {
        axios.get(`http://localhost:8000/shop/api/users/${userId}`)
            .then(response => {
                this.userDetails = response.data;
                let options = { year: 'numeric', month: 'long' }
                this.dateJoined = new Date(this.userDetails.date_joined).toLocaleDateString('en-US', options)
            })
            .catch(error => {
                console.error('Error fetching user details:', error);
            });
      }
    }
  };


</script>