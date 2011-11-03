# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/lewis
# catalog-date 2007-03-08 21:58:53 +0100
# catalog-license pd
# catalog-version 0.1
Name:		texlive-lewis
Version:	0.1
Release:	1
Summary:	Draw Lewis structures
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/lewis
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lewis.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lewis.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package provides rudimentary support for drawing Lewis
Structures. Support is limited to elements that support the
octet rule.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/lewis/lewis.sty
%doc %{_texmfdistdir}/doc/latex/lewis/README
%doc %{_texmfdistdir}/doc/latex/lewis/lewis.pdf
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}