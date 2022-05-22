FROM jboss/keycloak:12.0.4

WORKDIR /opt/jboss/keycloak
COPY  theme ./themes/unife-theme
COPY  imports ./imports
COPY  standalone.xml ./configuration/standalone.xml

CMD [ "-b 0.0.0.0 -Dkeycloak.profile.feature.upload_scripts=enabled -Dkeycloak.import=/opt/jboss/keycloak/imports/realm-export.json" ]