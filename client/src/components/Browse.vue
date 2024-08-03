<template>
    <div>
      <h3>Here you can browse all listings!</h3>
      <br>
      <div class="grid-container">
        <div v-for="(listing, index) in listings" :key="index" class="grid-item">
          <img :src="listing.photo" :alt="listing.title" />
          <p>{{ listing.title }}</p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'Listings',
    data() {
      return {
        listings: [],
      };
    },
    mounted() {
        console.log('Getting the data in a second!')
        axios.get('http://localhost:8000/shop/api/browse')
        .then(response => {
          console.log(response.data);
          this.listings = response.data;
        })
        .catch(error => {
          console.error('Error fetching listings:', error);
        });
    },
  };
  </script>
  
  <style>
  .grid-container {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
    padding: 20px;
  }
  .grid-item {
    border: 1px solid #ccc;
    padding: 10px;
    text-align: center;
    transition: transform 0.3s;
  }
  .grid-item img {
    max-width: 100%;
    height: auto;
  }
  .grid-item:hover {
    transform: scale(1.05);
  }
  </style>
  