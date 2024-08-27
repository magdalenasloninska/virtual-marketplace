<template>
    <Nav />

    <v-container class="pt-10">
        <v-row justify="center">
            <v-col cols="12" xl="8">
                <h3>Here you can add a new listing!</h3>
                <v-spacer class="pa-4"></v-spacer>
                
                <form>
                    <v-text-field
                        label="Title"
                        required
                        v-model="title"
                    ></v-text-field>

                    <v-select
                        label="Category"
                        :items="['Clothing',
                                 'Shoes',
                                 'Home & lifestyle',
                                 'Vintage']"
                    ></v-select>

                    <v-file-input
                        label="Photo"
                        v-model="photo"
                    ></v-file-input>

                    <v-textarea
                        label="Description"
                        variant="filled"
                        auto-grow
                        prepend-icon="mdi-text-box-edit"
                        rows="3"
                    ></v-textarea>

                    <v-text-field
                        label="Price"
                        type="number"
                        :min="0"
                        :max="1000"
                        prepend-icon="mdi-currency-eur"
                        v-model="price"
                    ></v-text-field>

                    <v-spacer class="pa-4"></v-spacer>

                    <v-btn
                        class="me-4"
                        color="rgb(199, 189, 231)"
                        v-on:click="publishListing()"
                    >
                        Publish
                    </v-btn>

                    <v-btn
                        class="me-4"
                        color="rgb(199, 189, 231)"
                        variant="outlined"
                    >
                        Save to drafts
                    </v-btn>
                </form>
            </v-col>
        </v-row>
    </v-container>
</template>

<style>
    .welcome_page_btn {
        font-size: 32px;
        text-transform: none;
    }

    .typewriter {
        font-family: 'Courier New', Courier, monospace;
    }

    .handwritten {
        font-family: 'Homemade Apple', cursive;
    }
</style>

<script>
    const items = [
        "Apparel",
        "Shoes",
        "Home & lifestyle",
        "Vintage"
    ]

    import axios from 'axios';

    export default {
        data() {
            return {
                title: '',
                photo: null,
                price: 0
            }
        },
        methods: {
            async publishListing() {
                let formData = new FormData()
                formData.append('title', this.title)
                formData.append('photo', this.photo)
                formData.append('price', this.price)

                let _ = await axios.post("http://localhost:8000/shop/api/listings/new/data", formData, {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                });
            }
        }
    }
</script>