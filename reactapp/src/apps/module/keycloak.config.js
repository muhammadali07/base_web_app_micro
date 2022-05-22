import Keycloak from 'keycloak-js';

export const keycloakConfig = {
    clientId: process.env.KEYCLOAK_CLIENT_FRONT || 'frontend',
    url: process.env.KEYCLOAK_AUTH_FRONT || 'http://localhost:8446/auth/',
    realm: process.env.KEYCLOAK_REALM || 'belajar1',
};

const keycloak = new Keycloak(keycloakConfig);

export default keycloak;
