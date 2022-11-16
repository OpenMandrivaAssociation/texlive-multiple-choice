Name:		texlive-multiple-choice
Version:	63722
Release:	1
Summary:	LaTeX package for multiple-choice questions
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/multiple-choice
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/multiple-choice.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/multiple-choice.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package adjusts the choices of the multiple-choice
question automatically. It has been wholly inspired by the work
of Enrico Gregorio and improved by Vafa Khalighi and I've just
packed and redistributed it under the name of the
multiple-choice package.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/multiple-choice
%doc %{_texmfdistdir}/doc/latex/multiple-choice

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
