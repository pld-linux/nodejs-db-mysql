%define		pkg	db-mysql
Summary:	MySQL database bindings for Node.js
Name:		nodejs-%{pkg}
Version:	0.7.6
Release:	1
License:	MIT
Group:		Development/Libraries
URL:		http://nodejsdb.org/db-mysql
Source0:	http://registry.npmjs.org/db-mysql/-/%{pkg}-%{version}.tgz
# Source0-md5:	1960ced1589fe901697472db2898d58d
Patch0:		library-path.patch
BuildRequires:	mysql-devel
BuildRequires:	nodejs-devel
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		nodejs_libdir %{_libdir}/node

%description
Node.js bindings to relational databases: MySQL database binding.

%prep
%setup -qc
mv package/* .
%patch0 -p1

%build
NODE_PATH=%{nodejs_libdir}/%{pkg} \
node-waf configure build

%install
rm -rf $RPM_BUILD_ROOT
node-waf install \
	--destdir=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}
cp -p %{pkg}.js package.json $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%dir %{nodejs_libdir}/%{pkg}
%{nodejs_libdir}/%{pkg}/*.js
%{nodejs_libdir}/%{pkg}/package.json
%attr(755,root,root) %{nodejs_libdir}/%{pkg}/mysql_bindings.node
