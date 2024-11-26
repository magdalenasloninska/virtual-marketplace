<template>
    <Nav />

    <v-container class="pt-10">
        <v-row justify="center">
            <v-col cols="12" xl="8">
                <h3>Here you can add a new listing!</h3>
                <v-spacer class="pa-4"></v-spacer>

                <div>
                    <v-alert
                        v-if="successAlert"
                        close-label="Close Alert"
                        color="rgb(215, 235, 186)"
                        type="success"
                        closable
                        class="mb-8"
                    >
                        The listing has been published successfuly!
                    </v-alert>
                    
                    <v-alert
                        v-if="errorAlert"
                        color="rgb(216, 30, 91)"
                        type="error"
                        closable
                        class="mb-8"
                    >
                        The listing couldn't be published, fix errors and try again!
                    </v-alert>
                </div>

                <v-row>
                    <v-col cols="6" class="d-flex justify-center">
                        <div>
                            <!-- <v-img
                                :src="photoPreview"
                                height="500"
                                width="500"
                            ></v-img> -->

                            <v-card
                                class="mt mb-8"
                                variant="outlined"
                                height="500"
                                width="500"
                            >
                                <canvas
                                    id="editingCanvas"
                                    width="500"
                                    height="500"
                                ></canvas>
                            </v-card>

                            <v-switch
                                class="mt-4"
                                label="Drawing mode"
                                color="primary"
                                @change="toggleFreeDrawing"
                            ></v-switch>
                        </div>
<!--                 
                        <v-card
                            class="d-flex justify-center align-center"
                            variant="outlined"
                            height="500"
                            width="500"
                            style="color: lightgrey;"
                        >
                            <v-card-title
                                class="typewriter"
                            >
                                Photo preview here
                            </v-card-title>    
                        </v-card> -->
                    </v-col>
                    <v-col cols="6">
                        <form>
                            <v-text-field
                                label="Title"
                                required
                                v-model="title"
                            ></v-text-field>

                            <v-select
                                label="Category"
                                :items=categories
                                item-title="text"
                                item-value="value"
                                v-model="selectedCategory"
                            ></v-select>

                            <v-file-input
                                label="Photo"
                                @change="generatePreview"
                                @click:clear="photoPreview = null;"
                                v-model="photo"
                            ></v-file-input>

                            <v-textarea
                                label="Description"
                                variant="filled"
                                auto-grow
                                prepend-icon="mdi-text-box-edit"
                                rows="3"
                                v-model="description"
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
                                v-on:click="publishListing"
                            >
                                Publish
                            </v-btn>

                            <v-btn
                                class="me-4"
                                color="rgb(199, 189, 231)"
                                variant="outlined"
                                @click="this.$router.push('/listings/fabric')"
                            >
                                Save to drafts
                            </v-btn>
                        </form>

                    </v-col>
                </v-row>
            </v-col>
        </v-row>
    </v-container>
</template>

<style>
    .typewriter {
        font-family: 'Courier New', Courier, monospace;
    }

    .handwritten {
        font-family: 'Homemade Apple', cursive;
    }
</style>

<script>
    import axios from 'axios';
    import * as fabric from 'fabric';

    export default {
        data() {
            return {
                categories: [],
                title: '',
                description: '',
                selectedCategory: null,
                photo: null,
                photoPreview: null,
                price: 0,
                currentUserId: null,
                successAlert: false,
                errorAlert: false,

                // Fabric.js canvas options
                canvas: null,
                isDrawing: false,
                brushColour: "#c7bde7"
            }
        },
        mounted() {
            this.fetchAllItemCategories();
            this.getCurrentUser();
            this.setupCanvas();
        },
        methods: {
            fetchAllItemCategories() {
                axios.get('http://localhost:8000/shop/api/listings/categories')
                .then(response => {
                    this.categories = response.data.categories;
                })
                .catch(error => {
                    console.error('Error fetching item categories:', error);
                });
            },
            async publishListing() {
                let formData = new FormData();
                formData.append('title', this.title);
                formData.append('category', this.selectedCategory);
                formData.append('photo', this.photo);
                formData.append('description', this.description);
                formData.append('price', this.price);
                formData.append('id', this.currentUserId);

                let _ = await axios.post("http://localhost:8000/shop/api/listings/new/data", formData, {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                })
                .then(response => {
                    console.log(response.data.message);

                    if (response.data.success) {
                        this.successAlert = true;
                        this.errorAlert = false;
                    } else {
                        this.successAlert = false;
                        this.errorAlert = true;
                    }
                    
                })
                .catch(error => {
                    console.error('Error publishing new listing:', error);
                    this.successAlert = false;
                    this.errorAlert = true;
                });
            },
            getCurrentUser() {
                axios.get('http://localhost:8000/shop/api/users/current-user')
                    .then(response => {
                        if (response.data.username) {
                            this.currentUserId = response.data.id;
                        }
                    })
                    .catch(error => {
                        console.error(`Error fetching current user: ${error}`);
                    });
            },
            generatePreview(event) {
                const file = event.target?.files?.[0];
                if (file) {
                    this.photo = file;
                    this.photoPreview = URL.createObjectURL(file);
                }

                fabric.Image.fromURL(this.photoPreview).then((img) => {
                    
                    let scale = Math.min(500 / img.height, 500 / img.width);

                    img.set({
                            dirty: true,
                            scaleX: scale,
                            scaleY: scale,
                            left: 0,
                            top: 0,
                            selectable: false,
                            evented: false,
                            hasControls: false
                    });

                    this.canvas.add(img);
                    this.canvas.centerObject(img);
                });
            },
            setupCanvas() {
                this.canvas = new fabric.Canvas('editingCanvas', {
                    width: 500,
                    height: 500
                });

                this.canvas.freeDrawingBrush = new fabric.PencilBrush(this.canvas);
                this.canvas.freeDrawingBrush.color = this.brushColour;
                this.canvas.freeDrawingBrush.width = 10;
            },
            toggleFreeDrawing() {
                this.isDrawing = !this.isDrawing;
                this.canvas.isDrawingMode = this.isDrawing;

                if (this.isDrawing) {
                    this.canvas.freeDrawingBrush.color = this.brushColour;
                }

                console.log('Toggle!');
            }
        }
    }
</script>