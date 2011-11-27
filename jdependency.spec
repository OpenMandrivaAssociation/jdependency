Name:           jdependency
Version:        0.6
Release:        6
Summary:        This project provides an API to analyse class dependencies

Group:          Development/Java
License:        ASL 2.0
URL:            http://github.com/tcurdt/jdependency
# wget http://github.com/tcurdt/jdependency/tarball/jdependency-0.6
Source0:        tcurdt-jdependency-jdependency-0.6-0-g165c94a.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch: noarch

BuildRequires:     maven2
BuildRequires:     maven2-common-poms
BuildRequires:     maven2-plugin-compiler
BuildRequires:     maven2-plugin-install
BuildRequires:     maven2-plugin-jar
BuildRequires:     maven2-plugin-javadoc
BuildRequires:     maven2-plugin-resources
BuildRequires:     maven2-plugin-surefire
BuildRequires:     maven2-plugin-idea

BuildRequires:  jpackage-utils 
BuildRequires:  java-devel
BuildRequires:  objectweb-asm
BuildRequires:  apache-commons-io
Requires:  objectweb-asm >= 3.2
Requires:  apache-commons-io
Requires:  java 

Requires(post):    jpackage-utils 
Requires(postun):  jpackage-utils 


%description
jdependency is small library that helps you analyze class level 
dependencies, clashes and missing classes.

%package javadoc
Group:          Development/Java
Summary:        API documentation for %{name}
Requires:       jpackage-utils

%description javadoc
%{summary}.


%prep
%setup -q -n tcurdt-jdependency-ae4617e 

%build
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p $MAVEN_REPO_LOCAL

mvn-jpp \
    -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
    install javadoc:javadoc

%install
rm -rf %{buildroot}

# Jar
mkdir -p %{buildroot}%{_javadir}
install -Dpm 644  target/%{name}-%{version}.jar  \
    %{buildroot}%{_javadir}/%{name}-%{version}.jar

pushd %{buildroot}%{_javadir}/
ln -s %{name}-%{version}.jar %{name}.jar
popd

# create a symbolic  link without the version
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; \
    do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# Javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}-%{version}/
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}
rm -rf target/site/api*


# poms
install -Dpm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-jdependency.pom

%add_to_maven_depmap org.vafer %{name} %{version} JPP %{name}

%post
%update_maven_depmap

%postun
%update_maven_depmap

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%doc LICENSE.txt README.md

%files javadoc
%defattr(-,root,root,-)
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}
%doc LICENSE.txt

