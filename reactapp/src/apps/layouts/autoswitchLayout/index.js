import React from 'react';
import { useKeycloak } from '@react-keycloak/web'
import Layouts from '..';

const AutoSwitchLayout = ({children}) => {

    // const { keycloak } = useKeycloak()
    // if(keycloak.authenticated)
        return(
            <Layouts>
                {children}
            </Layouts>
        )
    // return children
}
 
export default AutoSwitchLayout;