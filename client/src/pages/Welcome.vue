<template>
    <Nav />

    <div class="background-image">

        <v-container class="pt-10">
            <v-row justify="center">
                <v-col cols="12" xl="8">
                    <!-- <h1>Welcome to the most stylish corner of the internet!</h1> -->
                    <!-- <v-spacer class="pa-4"></v-spacer> -->
                    
                    <router-link to="/listings/browse/all" class="nav-link">
                        <v-btn
                            class="welcome_page_btn typewriter pa-4"
                            block
                            size="x-large"
                            color="secondary"
                        >
                            I'm buying
                        </v-btn>
                    </router-link>
                        
                    <v-spacer class="pa-4"></v-spacer>

                    <router-link to="/listings/new" class="nav-link">
                        <v-btn
                            class="welcome_page_btn handwritten pa-4"
                            block
                            size="x-large"
                            color="primary"
                        >
                            I'm selling
                        </v-btn>   
                    </router-link>
                </v-col>
            </v-row>
        </v-container>

    </div>
</template>

<style>
    .welcome_page_btn {
        font-size: 32px;
        text-transform: none;
    }

    .nav-link {
        text-decoration: none;
    }

    .typewriter {
        font-family: 'Courier New', Courier, monospace;
    }

    .handwritten {
        font-family: 'Homemade Apple', cursive;
    }

    .background-image {
        background-image: url('@/assets/car.JPEG');
        background-size: cover;
        background-position: top;
        background-repeat: no-repeat;
        overflow: hidden;
    
        /* Viewport settings */
        height: 100vh;  
        width: 100vw;
}
</style>