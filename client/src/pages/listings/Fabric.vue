<template>
    <Nav />

    <v-container class="pt-10">
        <v-row justify="center">
            <v-col cols="12" xl="8">
                <h3>Here you can test out Fabric.js!</h3>

                <v-card
                    class="mt-8 mb-8"
                    variant="outlined"
                    height="400"
                    width="400"
                    style="overflow: visible;"
                >
                    <canvas
                        id="drawingCanvas"
                        width="400"
                        height="400"
                    ></canvas>
                </v-card>

                <v-switch
                    label="Drawing mode"
                    color="primary"
                    @change="toggleFreeDrawing"
                ></v-switch>
            </v-col>
        </v-row>
    </v-container>
</template>

<style>
</style>

<script>
    import * as fabric from 'fabric';
    import { FabricImage } from 'fabric';
    import dressImage from '@/assets/dress.jpeg';


    export default {
        data() {
            return {
                canvas: null,
                isDrawing: false,
                brushColour: "#c7bde7"
            };
        },
        mounted() {
            this.initializeCanvas();
        },
        methods: {
            initializeCanvas() {
                this.canvas = new fabric.Canvas('drawingCanvas', {
                    width: 400,
                    height: 400,
                    backgroundColor: null
                });

                this.canvas.freeDrawingBrush = new fabric.PencilBrush(this.canvas);
                this.canvas.freeDrawingBrush.color = this.brushColour;
                this.canvas.freeDrawingBrush.width = 5;

                fabric.Image.fromURL(dressImage).then((img) => {
                    img.set({
                            dirty: true,
                            scaleX: 1,
                            scaleY: 1,
                            left: 0,
                            top: 0,
                            selectable: false,
                            evented: false,
                            hasControls: false          
                    });

                    this.canvas.add(img);
                    this.canvas.setActiveObject(img);
                });

                console.log('After setupCanvas:', document.getElementById('drawingCanvas'));
            },
            toggleFreeDrawing() {
                this.isDrawing = !this.isDrawing;
                this.canvas.isDrawingMode = this.isDrawing;

                if (this.isDrawing) {
                    this.canvas.freeDrawingBrush.color = this.brushColour;
                }

                console.log('Free drawing switched on!');
            },
            saveCanvas() {
                const dataURL = this.canvas.toDataURL();
                console.log('Canvas saved image URL:', dataURL);
            }
        }
    };

</script>