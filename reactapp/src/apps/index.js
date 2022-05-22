import React, { Suspense, useEffect } from 'react';
import { BrowserRouter as Router, Switch } from 'react-router-dom';
import { SwitchRouter } from './router';
import { useKeycloak } from '@react-keycloak/web';
import { AutoSwitchLayout } from './layouts';
import { LoadingIcon } from './components';

const AppIndex = () => {
    // const {keycloak, initialized} = useKeycloak();

    // if(!initialized)
    //     return(
    //         <div style={{
    //             margin:"auto",
    //             width: "fit-content",
    //             paddingTop: "20%",
    //             textAlign:"center"
    //         }}>
    //             <LoadingIcon width="100px" />
    //             <h5 className="text-base">Initializing User</h5>
    //         </div>
    //     )
    return ( 
        <>
            <Router basename="/">
                <AutoSwitchLayout>
                    <SwitchRouter />
                </AutoSwitchLayout>
            </Router>
        </>
     );
}
 
export default AppIndex;