# Conversion guide

## Introduction

This guide outlines how to convert existing code based on legacy versions of this
library to be compatible to current versions.  
Whenever a new breaking change in the library is introduced, a new section
will be added here, explaining how to convert existing code using this library
to overcome these breaking changes.  
Each section gives the involved (master-)commit, so it is up to the user to identify
the commit range used in their local copy, and apply each conversion from bottom to top
subsequently, to update to the newest version.

## Conversions

### Feature Hierarchy Rework

Commit: TBD

#### Involved parts

- ICs
- Modules
- EvalBoards

#### Outline

Entire mapping of hardware hierarchy has been reworked. The way of accessing parameters
has been unified and simplified for most use cases. Feature implementations have
been introduced via inheritance.

#### Conversion

##### Accessing fields
