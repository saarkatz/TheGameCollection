# The Space System
The space system is meant to support different special working environments as well as support multiple environments
simultaneously. All while providing mathematical constructs needed in the supported environments.
The space system should also provide the required infrastructure to translate and customize visual information from the
supported environments to the 2-Dimensional space of the screen.

## Space 2D
```import engine.space.space2d```\
This space is used for the screen space as well as a 2D environment for the game.
This is the space with the simples camera system as there is little to no translation needed between 2D environment and
the screen space. However, the camera system can still be used to augment modify and customize the view of the
environment.

### Space 2D would include
- Transform
    - position
    - rotation
    - scale
- Vector (Immutable)
    - arithmetic opperations
- Primitive Members (Primitives)
    - regular shapes
    - polygon shapes
    - parametric curve shapes
- Asset Support
    - image support (static/dynamic)
    - Modification infrastructure
        - Slicing/Stitching
        - Dynamic construction
- Camera (Cast to 2D surface)
    - transform
    - camera parameters (visual effects)
        - resolution
        - contrast
        - colors
    - Anti-Aliasing