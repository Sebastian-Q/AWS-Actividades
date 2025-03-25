import React, { useState, useEffect } from "react";
import axios from "axios";

const CustomUserForm = () => {
    const [formFields, setFormFields] = useState([]);
    const [formData, setFormData] = useState({
        email: "",
        password: "",
        name: "",
        surname: "",
        control_number: "",
        age: "",
        tel: "",
    });

    useEffect(() => {
        axios.get("http://127.0.0.1:8000/users/form/")
        .then((response) => {
            console.log("setFormFields: ", response.data); // Verifica que los datos se reciban correctamente
            setFormFields(response.data);
        })
        .catch((error) => console.error("Error al obtener los datos",error));
    }, []);

    const handleInputChange = (event) => {
        const { name, value } = event.target;
        setFormData((field) => ({
            ...field,
            [name]: value, // Usa el nombre del campo para actualizar el estado
        }));
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        console.log("formData: ", formData);
        // Enviar la solicitud POST para registrar el usuario
        axios.post("http://127.0.0.1:8000/users/form/", formData)
        .then((response) => {
            alert(response.data.message); // Mensaje de éxito
        })
        .catch((error) => {
            alert("Hubo un error al crear el usuario.");
            console.error("Error al enviar el formulario", error);
        });
    };

    return (
        <div>
            <h1>Nuevo Usuario</h1>
            
            <form onSubmit={handleSubmit}>
                {formFields && Object.keys(formFields).map((field, index) => {
                    const { label, input, type, name } = formFields[field]; // Asegúrate de que 'name' existe en la respuesta
                    return (
                        <div key={field}>
                            <label htmlFor={name}>{label}</label>
                            <input
                                {...input}
                                id={name} // Asegura que tenga un ID único
                                name={name} // Usa 'name' en lugar de 'field' o 'index'
                                value={formData[name] || ""} // Asegura que coincida con los datos enviados
                                onChange={handleInputChange}
                                type={type || "text"}
                            />
                            {/* Mostrar las condiciones si el campo es password */}
                            {field === "password" && (
                                <div>
                                    <p>Al menos un número.</p>
                                    <p>Al menos una letra mayúscula.</p>
                                    <p>Al menos un carácter especial (!#$%&?).</p>
                                    <p>Mínimo de 8 caracteres en total.</p>
                                </div>
                            )}
                            <br />
                        </div>
                    );
                })}
                <button type="submit">Enviar</button>
            </form>
        </div>
    );
}

export default CustomUserForm;