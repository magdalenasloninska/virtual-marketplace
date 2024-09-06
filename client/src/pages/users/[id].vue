<template>
    <Nav/>
  
    <v-container class="pt-10">
      <v-row justify="center">
        <v-col cols="4" xl="3">
          <v-responsive>
            <v-avatar size="300">
              <v-img
                :src="userDetails.profile_picture"
              ></v-img>
            </v-avatar>
          </v-responsive>
        </v-col>
  
        <v-col cols="8" xl="5">
          <v-card>
            <v-card-title>
              <h1>{{ userDetails.username }}</h1>
            </v-card-title>
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
          <h3>Here you can view all of {{ userDetails.username }}'s listings!</h3>
        </v-col>
      </v-row>
    </v-container>
  
  </template>
  
  <style scoped>
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