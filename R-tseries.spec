%global packname  tseries
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.10.32
Release:          1
Summary:          Time series analysis and computational finance
Group:            Sciences/Mathematics
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/tseries_0.10-32.tar.gz
Requires:         R-quadprog R-stats R-zoo R-graphics R-stats R-utils R-its
BuildRequires:    R-devel Rmath-devel texlive-collection-latex
BuildRequires:    R-quadprog R-stats R-zoo R-graphics R-stats R-utils R-its
BuildRequires:    blas-devel
BuildRequires:    lapack-devel

%description
Package for time series analysis and computational finance

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
