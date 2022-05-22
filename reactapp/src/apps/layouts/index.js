import React, { memo } from 'react';
import Navbar from './navbar';
import Sidebar from './sidebar';
const Layouts = memo(({children}) => {
    return (
        <>
            <div className="wrapper">
               <Navbar />
                {/* <!-- Main Sidebar Container --> */}
               <Sidebar />
                {/* <!-- Content Wrapper. Contains page content --> */}
                <div className="content-wrapper">
                    {/* <!-- Content Header (Page header) --> */}
                    <section className="content-header">
                        <div className="container-fluid">
                            <div className="row mb-2">
                                <div className="col-sm-12">
                                    <ol className="breadcrumb float-md-left float-sm-right">
                                        <li className="breadcrumb-item"><a href="#">Home</a></li>
                                        <li className="breadcrumb-item"><a href="#">Layout</a></li>
                                        <li className="breadcrumb-item active">Fixed Layout</li>
                                    </ol>
                                </div>
                            </div>
                        </div>
                    {/* <!-- /.container-fluid --> */}
                    </section>

                    {/* <!-- Main content --> */}
                    <section className="content">
                        <div className="container-fluid">
                            {children}
                        </div>
                    </section>
                    {/* <!-- /.content --> */}
                </div>
  {/* <!-- /.content-wrapper --> */}
            </div>

        </>
    );
})

export default Layouts;
export { default as AutoSwitchLayout } from './autoswitchLayout'