import React from 'react';
import { Link, useLocation } from 'react-router-dom';

const Sidemenu = ({
    hasChild = false,
    childs = [],
    name = "Nama Menu",
    url = undefined,
    icon = "far fa-bullet-o",
    iconType = "css",
    active = false,
    badge,
    onClick = ()=> null,
    childMode = false
}) => {

    if(hasChild)
        return (
            <>
                <a href="#" className={`nav-link ${active ? "active" : ""}`}>
                    {
                        iconType === "css" ? <i className={`nav-icon ${icon}`}></i> : (
                            icon
                        )
                    }
                    <p>
                        {name}
                        <i className="right fas fa-angle-left"></i>
                        {badge && badge}
                    </p>
                </a>
                <CreateChild
                    childs={childs}
                    active={active}
                />
          
            </>
        )

    return ( 
        <>
           
            <Link to={url} className={`nav-link ${active ? "active" : ""}`}>
                {
                    iconType === "css" ? <i className={`nav-icon ${icon}`}></i> : (
                        icon
                    )
                }
                <p>
                    {name}
                    {badge && badge}
                </p>
            </Link>
        </>
     );
}
 
function CreateChild({ 
    childs
}) {

    const location = useLocation();
    return <ul className="nav nav-treeview">
        {
            childs.map((c,a)=>(
                <li key={a} className="nav-item">
                    <Sidemenu {
                        ...{
                                ...c, 
                                active:(location.pathname === c.url), 
                                name:(location.pathname === c.url) ? <b> {c.name} </b> : c.name
                            }
                        } 
                    />
                </li>
            ))
        }
    </ul>
        
}
export default Sidemenu;

