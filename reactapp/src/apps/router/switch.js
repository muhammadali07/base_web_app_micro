import React, { Suspense } from 'react';
import { Route, Switch } from 'react-router-dom';
import { Dashboard, Test } from '../pages';

export default function (){


    return(
        <>
            <Switch>
                <Suspense fallback={<h1>Loading</h1>}>
                    <Route
                        key="/"
                        path="/"
                        exact={true}
                        render={(props)=><Dashboard { ...props} />}
                    />
                    <Route
                        key="/test"
                        path="/test"
                        exact={true}
                        render={(props)=> <Test { ...props} />}
                    />
                </Suspense>
            </Switch>
        </>
    )
}