import React, { useState, useEffect } from "react";
import DataTable from "react-data-table-component";
import axios from "axios"; // Si deseas obtener datos desde una API
import Swal from "sweetalert2";

const UserDataTable = () => {
  const [data, setData] = useState([]); // Datos para la tabla
  const [loading, setLoading] = useState(true); // Estado de carga

  const [showEdit, setShowEdit] = useState(false);
  const [selectedUser, setSelectedUser] = useState(null);

  // Configuración de columnas
  const columns = [
    {
      name: "Nombre",
      selector: (row) => row.name, // Selector de datos
      sortable: true, // Habilitar ordenamiento
    },
    {
      name: "Email",
      selector: (row) => row.email,
      sortable: true,
    },
    {
      name: "Teléfono",
      selector: (row) => row.tel,
    },
    {
      name: "Acciones",
      cell: (row) => {
        const currentEmail = localStorage.getItem("email");
        const isOwnUser = currentEmail === row.email;
        return (
          <span>
            <button
              className="btn btn-warning me-2"
              onClick={() => {
                
                setSelectedUser(row);
                setShowEdit(true);
              }}
            >
              <i className="bi bi-pencil"></i>
            </button>
    
            {!isOwnUser && (
              <button
                className="btn btn-danger me-2"
                onClick={() => {
                  Swal.fire({
                        title: 'Eliminación de usuario',
                        text: `¿Estás seguro de que deseas eliminar a ${row.name}?`,
                        icon: "warning",
                        showCancelButton: true,
                        confirmButtonColor: "#d33",
                        cancelButtonColor: "#6B6B6B",
                        confirmButtonText: "Eliminar",
                        cancelButtonText: "Cancelar",
                      }).then((result) => {
                        if (result.isConfirmed) {
                          axios.delete(
                              `http://127.0.0.1:8000/users/api/${row.id}/`,
                              {
                                headers: {
                                  Authorization: `Bearer ${localStorage.getItem("accessToken")}`,
                                },
                              }
                            )
                            .then(() => {
                              setData(data.filter((user) => user.id !== row.id));
                              Swal.fire({
                                toast: true,
                                position: 'top-end',
                                icon: 'success',
                                title: 'Usuario actualizado correctamente',
                                showConfirmButton: false,
                                timer: 2000,
                                timerProgressBar: true,
                              });
                            })
                            .catch((error) => {
                              Swal.fire({
                                toast: true,
                                position: 'top-end',
                                icon: 'error',
                                title: 'Error al elimnar usuario',
                                showConfirmButton: false,
                                timer: 3000,
                                timerProgressBar: true,
                              });
                              refreshAccessToken();
                            });
                        }
                  });
                }}
              >
                <i className="bi bi-trash"></i>
              </button>
            )}
          </span>
        );
      },
    },
  ];

  // Obtener datos desde una API (puedes cambiar esta parte)
  useEffect(() => {
      axios
      .get("http://127.0.0.1:8000/users/api/")
      .then((response) => {
        setData(response.data);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error al cargar los datos:", error);
        setLoading(false);
      });
  }, []);

  const refreshAccessToken = async () => {
    try {
      const refresh = localStorage.getItem("refreshToken");
      const response = await axios.post("http://127.0.0.1:8000/users/token/refresh/", { refresh });
      const newAccessToken = response.data.access;
      localStorage.setItem("accessToken", newAccessToken);
    } catch (error) {
      console.error("Error al refrescar el token", error);
    }
  };

  const updateUser = async () => {
    Swal.fire({
      title: 'Actualizar usuario',
      text: `¿Estás seguro de que deseas actualizar a ${selectedUser.name}?`,
      icon: "warning",
      showCancelButton: true,
      confirmButtonColor: "#3085d6",
      cancelButtonColor: "#d33",
      confirmButtonText: "Actualizar",
      cancelButtonText: "Cancelar",
    }).then((result) => {
      if (result.isConfirmed) {
        axios.put(
            `http://127.0.0.1:8000/users/api/${selectedUser.id}/`, selectedUser,
            {
              headers: {
                Authorization: `Bearer ${localStorage.getItem("accessToken")}`,
              },
            }
          )
          .then(() => {
            Swal.fire({
              toast: true,
              position: 'top-end',
              icon: 'success',
              title: 'Usuario actualizado correctamente',
              showConfirmButton: false,
              timer: 2000,
              timerProgressBar: true,
            });

            setData((prevData) =>
              prevData.map((user) =>
                user.id === selectedUser.id ? selectedUser : user
              )
            );
            setShowEdit(false);
          })
          .catch((error) => {
            Swal.fire({
              toast: true,
              position: 'top-end',
              icon: 'error',
              title: 'Error al actualizar usuario',
              showConfirmButton: false,
              timer: 3000,
              timerProgressBar: true,
            });
            console.error("Error al actualizar usuario:", error);
            refreshAccessToken();
          });
      }
    });
  };

  return (
    <div>
      <h3>Tabla de usuarios</h3>
      <DataTable
        columns={columns}
        data={data}
        progressPending={loading}
        pagination
        highlightOnHover
        pointerOnHover
      />

      {showEdit && selectedUser && (
        <div className="modal d-block" tabIndex="-1" role="dialog" style={{backgroundColor: "rgba(0,0,0,0.5)"}}>
          <div className="modal-dialog modal-dialog-centered" role="document">
            <div className="modal-content">
              <div className="modal-header">
                <h5 className="modal-title">Editar Usuario</h5>
                <button type="button" className="btn-close" onClick={() => setShowEdit(false)}></button>
              </div>
              <div className="modal-body">
                <form>
                  <div className="row mb-3">
                    <div className="col-md-6 text-start">
                      <label className="form-label">Nombre</label>
                      <input
                        type="text"
                        className="form-control"
                        value={selectedUser.name}
                        onChange={(e) =>
                          setSelectedUser({ ...selectedUser, name: e.target.value })
                        }
                      />
                    </div>
                    <div className="col-md-6 text-start">
                      <label className="form-label">Apellido</label>
                      <input
                        type="text"
                        className="form-control"
                        value={selectedUser.surname}
                        onChange={(e) =>
                          setSelectedUser({ ...selectedUser, surname: e.target.value })
                        }
                      />
                    </div>
                  </div>

                  <div className="row mb-3">
                    <div className="col-md-8 text-start">
                      <label className="form-label">Email</label>
                      <input
                        type="email"
                        className="form-control"
                        value={selectedUser.email}
                        onChange={(e) =>
                          setSelectedUser({ ...selectedUser, email: e.target.value })
                        }
                      />
                    </div>
                    <div className="col-md-4 text-start">
                      <label className="form-label">Edad</label>
                      <input
                        type="number"
                        className="form-control"
                        value={selectedUser.age}
                        onChange={(e) =>
                          setSelectedUser({ ...selectedUser, age: e.target.value })
                        }
                      />
                    </div>
                  </div>

                  <div className="row mb-3 text-start">
                    <div className="col-md-6">
                      <label className="form-label">Teléfono</label>
                      <input
                        type="text"
                        className="form-control"
                        value={selectedUser.tel}
                        onChange={(e) =>
                          setSelectedUser({ ...selectedUser, tel: e.target.value })
                        }
                      />
                    </div>
                    <div className="col-md-6 text-start">
                      <label className="form-label">Núm Control</label>
                      <input
                        type="text"
                        className="form-control"
                        value={selectedUser.control_number}
                        onChange={(e) =>
                          setSelectedUser({ ...selectedUser, control_number: e.target.value })
                        }
                      />
                    </div>
                  </div>
                </form>
              </div>
              <div className="modal-footer">
                <button
                  type="button"
                  className="btn btn-primary"
                  onClick={() => {
                    console.log("Usuario actualizado:", selectedUser);
                    updateUser();
                  }}
                >
                  Actualizar
                </button>
                <button
                  type="button"
                  className="btn btn-secondary"
                  onClick={() => setShowEdit(false)}
                >
                  Cancelar
                </button>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>


    
  );
};

export default UserDataTable;
