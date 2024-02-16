import gradio as gr
import tensorflow as tf

def reconocer_digito(modelo_archivo, imagen):
    modelo = tf.keras.models.load_model(modelo_archivo.name)

    if imagen is not None:
        imagen = imagen.reshape((1, 28, 28, 1)).astype('float32') / 255

        prediction = modelo.predict(imagen)

        clases = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        confianza = [float(prediction[0][i]) for i in range(10)]

        return {clases[i]: confianza[i] for i in range(10)}
    else:
        return {}

with gr.Blocks() as app:
    gr.Markdown("<h1 style='text-align: center;'>Interfaz de Testeo para Modelos MNIST</h1>")
    gr.Markdown("<p style='font-size: 20px;'>Subí tu modelo y dibuja un número en el canvas para ver la clasificación.</p>")
    with gr.Row():
        inp1 = gr.File(label="Subir tu modelo clasificador MNIST (.h5/.hdf5/.keras)")
        gr.Examples(inputs=[inp1], examples=[["modelo_mnist_0_4171.h5"],["modelo_mnist_0_9735.h5"]], label="Ejemplos de modelos ya entrenados")
    with gr.Row():
        inp2 = gr.Image(shape=(28, 28), image_mode='L', invert_colors=True, source='canvas', label="Dibuja un número")
        out = gr.Label(num_top_classes=10, label="Clasificación del número dibujado")
    gr.ClearButton(components=[inp2, out], value="Borrar")
    inp2.change(reconocer_digito, inputs=[inp1, inp2], outputs=out)
    gr.Markdown("<p style='text-align: center;'><strong><em style='font-size: 20px;'>Creado por Luciano Esperlazza</em></strong></p>")
app.launch()