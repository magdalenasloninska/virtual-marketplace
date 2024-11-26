<template>
    <Nav />

    <v-container class="pt-10">
        <v-row justify="center">
            <v-col cols="12" xl="8">
                <h3>Here you can add your own request!</h3>

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
                        The request has been published successfuly!
                    </v-alert>
                    
                    <v-alert
                        v-if="errorAlert"
                        color="rgb(216, 30, 91)"
                        type="error"
                        closable
                        class="mb-8"
                    >
                        The request couldn't be published, fix errors and try again!
                    </v-alert>
                </div>

                <form>
                    <v-text-field
                        label="Title"
                        required
                        v-model="title"
                    ></v-text-field>

                    <v-textarea
                        label="Description"
                        variant="filled"
                        auto-grow
                        prepend-icon="mdi-text-box-edit"
                        rows="3"
                        v-model="description"
                    ></v-textarea>

                    <v-spacer class="pa-4"></v-spacer>

                    <v-btn
                        class="me-4"
                        color="rgb(199, 189, 231)"
                        @click="publishRequest()"
                    >
                        Publish
                    </v-btn>
                </form>
            </v-col>
        </v-row>
    </v-container>
</template>

<style>
</style>

<script>
    import axios from 'axios';

    export default {
        data() {
            return {
                title: '',
                description: '',
                currentUserId: null,
                successAlert: false,
                errorAlert: false
            }
        },
        created() {
            this.getCurrentUser();
        },
        methods: {
            async publishRequest() {
                let formData = new FormData();
                formData.append('title', this.title);
                formData.append('description', this.description);
                formData.append('id', this.currentUserId);

                let _ = await axios.post("http://localhost:8000/shop/api/listings/requests/new/data", formData)
                .then(response => {

                    if (response.data.success) {
                        this.successAlert = true;
                        this.errorAlert = false;
                    } else {
                        this.successAlert = false;
                        this.errorAlert = true;
                    }
                })
                .catch(error => {
                    console.error('Error publishing new request:', error);
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
            }
        }
    }
</script>