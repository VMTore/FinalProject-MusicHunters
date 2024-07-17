import React, { useContext } from "react";
import { Context } from "../store/appContext";
import rigoImageUrl from "../../img/rigo-baby.jpg";
import "../../styles/home.css";
import { Navbar } from "../component/navbar";
import { NavbarUser } from "../component/navbarUser";

export const HomeUser = () => {
  const { store, actions } = useContext(Context);

  return (
    <>
      <NavbarUser />
      <div className="container text-center mt-5">
        <h1 className="title-music-hunters">Music Hunters Home</h1>
        <h3 className="subtitle">
          Your website to find tickets to the best musical events at the best
          price!
        </h3>
        <div className="row justify-content-center mt-5 mb-5">
          <div className="card p-3 col-12 col-md-8 d-flex flex-row align-items-center">
            <img
              className="img-fluid"
              src="https://www.estupidafregona.net/wp-content/uploads/2023/12/mc2024-cabecera.png"
              alt="Music Event"
            />
          </div>
        </div>
      </div>
    </>
  );
};