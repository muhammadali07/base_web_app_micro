import React, { useEffect, useState } from 'react';
import { useLocation } from 'react-router';
import { Link } from 'react-router-dom';
import configLayout from '../../../layout.config';
import Sidemenu from './sidemenu';

function Sidebar(){

    const [keyOpened, setKeyOpened]  = useState(false);
    const menuItems = [
        {
            hasChild : false,
            name : "Dashboard",
            url : "/",
            icon : "fas fa-tachometer-alt",
            iconType : "css",
            badge : <></>,
            onClick : ()=> null
        },{
            
            hasChild : true,
            name : "Test",
            icon : "fas fa-columns",
            iconType : "css",
            childs : [
                {
                    hasChild : false,
                    name : "Index",
                    url : "/test",
                    iconType : "css",
                    onClick : ()=> null
                }
            ]
            
        },
        {
            
            hasChild : true,
            name : "Test",
            icon : "fas fa-columns",
            iconType : "css",
            childs : [
                {
                    hasChild : false,
                    name : "Index",
                    url : "/hh",
                    iconType : "css",
                    onClick : ()=> null
                }
            ]
            
        }
    ]


    const location = useLocation();
    const getActive = function(url, hasChild = false, child=[], key){
        if(hasChild)
            return child.some((v) => v.url === location.pathname) || key === keyOpened;
        return url === location.pathname
    }
    return(
        <>
            <aside className="main-sidebar sidebar-dark-primary elevation-2">
                {/* <!-- Brand Logo --> */}
                <a href="../../index3.html" className="brand-link text-center">
                    {/* <configLayout.logo height={300} width={25}/> */}
                    {/* <img src={configLayout.logo} alt="Logo" className="brand-image" style={{width:20}} /> */}
                    <span className="brand-text text-center font-weight-light">Learn APSS</span>
                </a>

                {/* <!-- Sidebar --> */}
                <div className="sidebar">
                {/* <!-- Sidebar Menu --> */}
                    <nav className="mt-2">
                        <ul className="nav nav-pills nav-sidebar flex-column nav-legacy nav-compact nav-child-indent nav-collapse-hide-child" data-widget="treeview" role="menu" data-accordion="false">
                        <li className="nav-item " style={{
                            borderBottom:"1px solid",
                            paddingTop:10,
                            paddingBottom:10
                        }}>
                            <Link to="/" className={`nav-link ${location.pathname === "/" ? "active" : ""}`} >
                                <i className="nav-icon fas fa-tachometer-alt">
                                </i>
                                <p>Dashboard</p>
                            </Link>
                        </li>
                        <li className="nav-header">EXAMPLES</li>
                        {/* <!-- Add icons to the links using the .nav-icon class
                            with font-awesome or any other icon font library --> */}
                            {
                                menuItems.map((p, i)=>(
                                    <li 
                                        onClick={ ()=> p.hasChild ? setKeyOpened(prevState => prevState === i ? false : i) : null } 
                                        className={`nav-item ${ (getActive(p.url, p.hasChild, p.childs,i) && p.hasChild ) ? "menu-is-opening menu-open" : ""}`}
                                    >
                                        <Sidemenu 
                                            key={i}
                                            { ... { ...p, active: getActive(p.url, p.hasChild, p.childs) }}
                                        />
                                    </li>
                                ))
                            }
                        </ul>
                    </nav>
                {/* <!-- /.sidebar-menu --> */}
                </div>
                {/* <!-- /.sidebar --> */}
            </aside>

        </>
    )
}

export default Sidebar;