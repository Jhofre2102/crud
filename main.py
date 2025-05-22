from flask import Flask, render_template, request, redirect , url_for
app=Flask(__name__)

usuario=[]
id_contador=1

@app.route ("/", methods=['GET', 'POST'])
def crud():
    global id_contador
    if request.method=="POST":
        nombre=request.form ["nombre"] 
        correo=request.form ["correo"]
        usuario.append({"id": id_contador, "nombre": nombre, "correo": correo})
        id_contador+=1
        #print(usuario)
    eliminar_id=request.args.get("eliminar")
    if eliminar_id:
        for diccionario in usuario:
            if str(diccionario["id"])==eliminar_id:
                usuario.remove(diccionario)
                break 

    return render_template ("crud.html", usuario=usuario)

@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    usuario_a_editar=''
    
    #TODO capturar el usuario a editar
    for diccionario in usuario:#para cada diccionario de la lista evalue
        if diccionario['id']==id: #si el id convertido a string es igual al id que se pasa  por parametros
            usuario_a_editar=diccionario #hemos identificado los datos del usuario a editar
            break
    #print(usuario_a_editar)
    
    #TODO actualizar la informacion del usuario seleccionado
    if request.method=="POST":
        usuario_a_editar["nombre"]=request.form.get("nombre")#el nombre nuevo seria el que llega por u nuevo formulario
        usuario_a_editar["correo"]=request.form.get("correo")
        return redirect(url_for("crud"))# redirecciona la aplicacion a la nota de la funcion crud


    if usuario_a_editar=='':
        return f"El usuario con Id {id} no se encuentra" 

    return render_template('editar.html',usuario_a_editar=usuario_a_editar)








if __name__=="__main__":
    app.run(debug=True)