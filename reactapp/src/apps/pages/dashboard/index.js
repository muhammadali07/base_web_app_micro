import React, { useEffect, useState } from 'react';
import { useKeycloak } from '@react-keycloak/web';
import { baseUrl } from '../../../config';
import { Button } from 'react-bootstrap';
import Layouts from "../../layouts";
import { LoadingIcon } from '../../components';

export default function(){
    // const {keycloak} = useKeycloak()
    const [dataUser, setDataUser] = useState({});

    // useEffect(function(){
    //     getUser()
    // },[])

    // async function getUser(){
    //     var opts  = {
    //         method: 'GET',
    //         headers: {
    //             Accept: 'application/json',
    //             'Content-Type': 'application/json',
    //             "Authorization" : `Bearer ${keycloak.token}`
    //         },
    //     }
    //     const resp = await fetch(`${baseUrl}auth-keycloak/me`, opts);
        
    //     const dataResp = await resp.json();
    //     console.log(dataResp)
    //     if(dataResp.response_code === "00")
    //         setDataUser(dataResp.data)
            
    // }

    return(
        <>
        <div className="card">
            <div className="card-body" style={{height:300}}>
                <div style={{
                    margin:"auto",
                    width: "fit-content",
                    paddingTop: "5%"
                }}>
                    <LoadingIcon width="100px" />
                </div>

            {/* {JSON.stringify(keycloak)} */}
            </div>
        </div>
        </>
    )
}