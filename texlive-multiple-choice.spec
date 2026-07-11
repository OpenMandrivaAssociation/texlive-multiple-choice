%global tl_name multiple-choice
%global tl_revision 63722

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	LaTeX package for multiple-choice questions
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/multiple-choice
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/multiple-choice.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/multiple-choice.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package adjusts the choices of the multiple-choice question
automatically. It has been wholly inspired by the work of Enrico
Gregorio and improved by Vafa Khalighi and I've just packed and
redistributed it under the name of the multiple-choice package.

