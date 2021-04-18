import pickle
from typing import Optional, List, Dict, Callable, IO

import ipywidgets as widgets
import k3d
import numpy as np
from IPython.display import display
from ipywidgets import Play, Checkbox, IntSlider, Button, ColorPicker, VBox, Tab
from k3d.plot import Plot

from .jointset import JointSet, MuPoTSJoints, OpenPoseJoints, CocoExJoints, PanopticJoints, Common14Joints
from .objects import Skeleton, DrawableSkeleton, Color, Positions


class FrameUpdater:
    def __init__(self, video_player: Play):
        self.video_player: Play = video_player

    def update_to_next_frame(self, button) -> None:
        if self.video_player.max > self.video_player.value:
            self.video_player.value += 1

    def update_to_previous_frame(self, button) -> None:
        if self.video_player.min < self.video_player.value:
            self.video_player.value -= 1


class ColorChanger:
    def __init__(self, skeleton: DrawableSkeleton, left_color_picker: ColorPicker,
                 right_color_picker: ColorPicker, center_color_picker: ColorPicker):
        self.skeleton: DrawableSkeleton = skeleton
        self.left_color_picker = left_color_picker
        self.right_color_picker = right_color_picker
        self.center_color_picker = center_color_picker

    def update_left_objects(self, current_color):
        for obj in self.skeleton.get_left_objects():
            obj.color = self.__get_as_hex_int(current_color.new)

    def update_right_objects(self, current_color):
        for obj in self.skeleton.get_right_objects():
            obj.color = self.__get_as_hex_int(current_color.new)

    def update_center_objects(self, current_color):
        for obj in self.skeleton.get_center_objects():
            obj.color = self.__get_as_hex_int(current_color.new)

    def update_all_objects(self, current_color):
        new_color = current_color.new
        for obj in self.skeleton:
            obj.color = self.__get_as_hex_int(new_color)
        self.left_color_picker.value = new_color
        self.right_color_picker.value = new_color
        self.center_color_picker.value = new_color

    @staticmethod
    def __get_as_hex_int(color: str):
        return int(color.replace('#', '0x'), 16)


class SkeletonVisualizer:
    """ A 3D skeleton visualizer which can visualize skeletons in 3D plots."""

    def __init__(self, joint_set: JointSet, size_scalar: float = 1.0):
        self.joint_set: JointSet = joint_set
        self.plot: Optional[Plot] = None
        self.size_scalar: float = size_scalar
        self.skeletons: List[DrawableSkeleton] = []
        self.joint_names_visible: Checkbox = Checkbox(description="Show Joint Names")
        self.joint_coordinates_visible: Checkbox = Checkbox(description="Show Coordinates")

    def visualize(self, skeletons: np.ndarray, colors: List[Color] = None, include_names: bool = False,
                  include_coordinates: bool = False, automatic_camera_orientation: bool = False,
                  is_gt_list: List[bool] = None) -> None:
        self.__assert_include_arguments(include_names, include_coordinates)
        self.__assert_skeleton_shapes(skeletons)
        colors = self.__init_colors(skeletons.shape[0], colors)
        if include_names:
            skeleton_converter = Skeleton.to_drawable_skeleton_with_names
        elif include_coordinates:
            skeleton_converter = Skeleton.to_drawable_skeleton_with_coordinates
        else:
            skeleton_converter = Skeleton.to_drawable_skeleton
        self.__create_skeleton_plot(skeletons=skeletons, skeleton_converter=skeleton_converter, colors=colors,
                                    automatic_camera_orientation=automatic_camera_orientation, is_gt_list=is_gt_list)
        self.plot.display()
        self.__display_checkboxes(include_names, include_coordinates)
        self.__display_color_changer()

    def visualize_with_ground_truths(self, pred_skeletons: np.ndarray, gt_skeletons: np.ndarray,
                                     pred_colors: List[Color] = None, gt_colors: List[Color] = None,
                                     include_names: bool = False, include_coordinates: bool = False,
                                     automatic_camera_orientation: bool = False) -> None:
        assert pred_skeletons.shape == gt_skeletons.shape, \
            'The predicate and ground truth skeleton arrays must have the same shape.'
        pred_colors = self.__init_colors(pred_skeletons.shape[0], pred_colors)
        gt_colors = self.__init_colors(gt_skeletons.shape[0], gt_colors)
        skeletons: np.ndarray = np.concatenate((pred_skeletons, gt_skeletons), axis=0)
        colors: List[Color] = pred_colors + gt_colors
        is_gt_list: List[bool] = [False] * len(pred_skeletons) + [True] * len(gt_skeletons)
        self.visualize(skeletons, colors, include_names, include_coordinates, automatic_camera_orientation, is_gt_list)

    def visualize_video_from_file(self, file_name: str, colors: List[Color] = None, fps: int = 15,
                                  include_names: bool = False, include_coordinates: bool = False,
                                  automatic_camera_orientation: bool = False) -> None:
        file: IO = open(file_name, 'rb')
        frames = pickle.load(file)
        file.close()
        self.visualize_video(frames, colors, fps, include_names, include_coordinates, automatic_camera_orientation)

    def visualize_video(self, frames: np.ndarray, colors: List[Color] = None, fps: int = 15,
                        include_names: bool = False, include_coordinates: bool = False,
                        automatic_camera_orientation: bool = False, is_gt_list: List[bool] = None) -> None:
        self.__assert_include_arguments(include_names, include_coordinates)
        assert len(frames.shape) == 4
        first_frame: np.ndarray = frames[0]
        self.__assert_skeleton_shapes(first_frame)
        colors = self.__init_colors(first_frame.shape[0], colors)
        skeleton_timestamps: List[Dict[str, np.ndarray]] = self.__get_skeleton_positions_timestamps(frames)
        if include_names:
            skeleton_converter = Skeleton.to_drawable_skeleton_for_video_with_names
        elif include_coordinates:
            skeleton_converter = Skeleton.to_drawable_skeleton_for_video_with_coordinates
        else:
            skeleton_converter = Skeleton.to_drawable_skeleton_for_video
        self.__create_skeleton_plot(skeletons=first_frame, skeleton_converter=skeleton_converter, colors=colors,
                                    positions=skeleton_timestamps,
                                    automatic_camera_orientation=automatic_camera_orientation, is_gt_list=is_gt_list)
        self.plot.display()
        self.__display_video_player(fps, frames)
        self.__display_checkboxes(include_names, include_coordinates)
        self.__display_color_changer()

    def visualize_video_with_ground_truths(self, pred_frames: np.ndarray, gt_frames: np.ndarray,
                                           pred_colors: List[Color] = None, gt_colors: List[Color] = None,
                                           fps: int = 15, include_names: bool = False,
                                           include_coordinates: bool = False,
                                           automatic_camera_orientation: bool = False):
        pred_colors = self.__init_colors(pred_frames.shape[1], pred_colors)
        gt_colors = self.__init_colors(gt_frames.shape[1], gt_colors)
        frames: np.ndarray = np.concatenate((pred_frames, gt_frames), axis=1)
        colors: List[Color] = pred_colors + gt_colors
        is_gt_list: List[bool] = [False] * len(pred_colors) + [True] * len(gt_colors)
        self.visualize_video(frames, colors, fps, include_names, include_coordinates,
                             automatic_camera_orientation, is_gt_list)

    def visualize_video_from_file_with_ground_truths(self, pred_file_name: str, gt_file_name: str,
                                                     pred_colors: List[Color] = None, gt_colors: List[Color] = None,
                                                     fps: int = 15, include_names: bool = False,
                                                     include_coordinates: bool = False,
                                                     automatic_camera_orientation: bool = False):
        file: IO = open(pred_file_name, 'rb')
        pred_frames = pickle.load(file)
        file.close()
        file = open(gt_file_name, 'rb')
        gt_frames = pickle.load(file)
        file.close()
        self.visualize_video_with_ground_truths(pred_frames, gt_frames, pred_colors, gt_colors, fps, include_names,
                                                include_coordinates, automatic_camera_orientation)

    @staticmethod
    def __get_skeleton_positions_timestamps(frames: np.ndarray) -> List[Dict[str, np.ndarray]]:
        frames_swapped: np.ndarray = np.swapaxes(frames, 0, 1)
        return [{
            str(timestamp_index): frames_swapped[current_frame_index][timestamp_index]
            for timestamp_index in range(len(frames_swapped[current_frame_index]))
        } for current_frame_index in range(len(frames_swapped))]

    def __create_skeleton_plot(self, skeletons: np.ndarray, skeleton_converter: Callable[[Skeleton], DrawableSkeleton],
                               colors: List[Color], positions: Optional[Positions] = None,
                               automatic_camera_orientation: bool = False, is_gt_list: List[bool] = None) -> None:
        self.__init_skeleton_plot(skeletons, automatic_camera_orientation)
        skeleton_part_size: float = self.__calculate_skeleton_part_size(skeletons)
        if positions is None:
            positions = skeletons
        skeletons: List[Skeleton] = self.__get_skeletons(positions, colors, skeleton_part_size, is_gt_list)
        drawable_skeletons: List[DrawableSkeleton] = list(map(skeleton_converter, skeletons))
        self.__add_skeletons_to_plot(drawable_skeletons)

    def __init_skeleton_plot(self, skeletons: np.ndarray, automatic_camera_orientation: bool = False) -> None:
        self.plot = k3d.plot(antialias=1, camera_auto_fit=False)
        centroid: np.ndarray = np.average(np.average(skeletons, axis=0), axis=0)
        if automatic_camera_orientation:
            camera_up_vector: np.ndarray = np.zeros(shape=(3,))
            for line_indices in self.joint_set.vertically_aligned_line_indices:
                camera_up_vector += np.sum(
                    skeletons[:, line_indices[1]] - skeletons[:, line_indices[0]],
                    axis=0)
            camera_up_vector /= np.linalg.norm(camera_up_vector, ord=2)
            self.plot.camera = [
                0.0, 0.0, 0.0,
                centroid[0], centroid[1], centroid[2],
                camera_up_vector[0], camera_up_vector[1], camera_up_vector[2]]
        else:
            self.plot.camera = [0.0, 0.0, 0.0, 0.0, 0.0, centroid[2], 0.0, -1.0, 0.0]

    def __calculate_skeleton_part_size(self, skeletons: np.ndarray) -> float:
        max_values = [abs(skeleton).max() for skeleton in skeletons]
        return (min(max_values) / 100.0) * self.size_scalar

    def __get_skeletons(self, positions: List[Positions], colors: List[Color],
                        skeleton_part_size: float, is_gt_list: List[bool] = None) -> List[Skeleton]:
        if is_gt_list is None:
            is_gt_list = [False] * len(colors)
        return list(map(lambda parameter_tuple: Skeleton(
            joint_positions=parameter_tuple[0],
            joint_set=self.joint_set,
            part_size=skeleton_part_size,
            color=parameter_tuple[1],
            is_ground_truth=parameter_tuple[2]
        ), zip(positions, colors, is_gt_list)))

    def __add_skeletons_to_plot(self, skeletons: List[DrawableSkeleton]) -> None:
        for drawable_skeleton in skeletons:
            self.plot += drawable_skeleton
            self.skeletons.append(drawable_skeleton)

    def __display_video_player(self, fps, frames) -> None:
        video_player: Play = Play(
            value=0,
            min=0, max=frames.shape[0] - 1,
            step=1, interval=1000 / fps,
            description='Press play', disabled=False)
        frame_updater = FrameUpdater(video_player)
        frame_slider = IntSlider(value=0, min=0, max=frames.shape[0] - 1, step=1, description='Frame')
        next_frame_button = Button(description='Next frame')
        next_frame_button.on_click(frame_updater.update_to_next_frame)
        previous_frame_button = Button(description='Previous frame')
        previous_frame_button.on_click(frame_updater.update_to_previous_frame)
        widgets.jslink((video_player, 'value'), (frame_slider, 'value'))
        widgets.jslink((video_player, 'value'), (self.plot, 'time'))
        display(widgets.HBox([video_player, previous_frame_button, frame_slider, next_frame_button]))

    @staticmethod
    def __init_colors(number_of_skeletons: int, colors: List[Color]) -> List[Color]:
        if colors is None:
            colors = ['default' for _ in range(number_of_skeletons)]
        else:
            assert number_of_skeletons == len(colors), \
                'The \'skeletons\' and \'colors\' parameters must be the same length.'
        return colors

    def __assert_skeleton_shapes(self, skeletons: np.ndarray) -> None:
        assert len(skeletons.shape) == 3, 'The \'skeletons\' parameter should be a 3 dimensional numpy array.'
        assert skeletons.shape[1] == self.joint_set.number_of_joints, \
            'The number of joints of skeletons and the number of joints in the specified joint set must be the same.'
        assert skeletons.shape[2] == 3, 'The skeleton joint coordinates must be 3 dimensional'

    @staticmethod
    def __assert_include_arguments(include_names: bool, include_coordinates: bool) -> None:
        if include_names is True and include_coordinates is True:
            raise AttributeError('Either names or coordinates can be showed, but not both.')

    def __display_checkboxes(self, include_names: bool, include_coordinates: bool) -> None:
        if include_names:
            self.__link_joint_name_visibility_with_checkbox()
            display(self.joint_names_visible)
        if include_coordinates:
            self.__link_joint_coordinate_visibility_with_checkbox()
            display(self.joint_coordinates_visible)

    def __link_joint_name_visibility_with_checkbox(self) -> None:
        for skeleton in self.skeletons:
            for joint_name in skeleton.joint_names:
                widgets.jslink((joint_name, 'visible'), (self.joint_names_visible, 'value'))

    def __link_joint_coordinate_visibility_with_checkbox(self) -> None:
        for skeleton in self.skeletons:
            for joint_coordinate in skeleton.joint_coordinates:
                widgets.jslink((joint_coordinate, 'visible'), (self.joint_coordinates_visible, 'value'))

    def __display_color_changer(self):
        children: List[VBox] = []
        pred_skeletons: List[DrawableSkeleton] = []
        gt_skeletons: List[DrawableSkeleton] = []
        for skeleton in self.skeletons:
            skeleton_color_changer_tab = self.__create_color_changer_tab([skeleton])
            children.append(skeleton_color_changer_tab)
            if skeleton.is_ground_truth:
                gt_skeletons.append(skeleton)
            else:
                pred_skeletons.append(skeleton)
        if len(pred_skeletons) != 0 and len(gt_skeletons) != 0:
            pred_skeleton_color_changer_tab: VBox = self.__create_color_changer_tab(pred_skeletons)
            gt_skeleton_color_changer_tab: VBox = self.__create_color_changer_tab(gt_skeletons)
            children.append(pred_skeleton_color_changer_tab)
            children.append(gt_skeleton_color_changer_tab)
        color_changer_widget: Tab = Tab(children=children)
        for i in range(len(self.skeletons)):
            color_changer_widget.set_title(i, 'Skeleton {:d} colors'.format(i + 1))
        if len(children) > len(self.skeletons):
            color_changer_widget.set_title(len(self.skeletons) + 1, 'Pred skeleton colors')
            color_changer_widget.set_title(len(self.skeletons) + 2, 'GT skeleton colors')
        display(color_changer_widget)

    def __create_color_changer_tab(self, skeletons: List[DrawableSkeleton]) -> VBox:
        left_color_picker: ColorPicker = ColorPicker(
            description='Left color:',
            value=self.__get_default_left_color(skeletons))
        right_color_picker: ColorPicker = ColorPicker(
            description='Right color:',
            value=self.__get_default_right_color(skeletons))
        center_color_picker: ColorPicker = ColorPicker(
            description='Center color:',
            value=self.__get_default_center_color(skeletons))
        all_color_picker: ColorPicker = ColorPicker(description='All color:', value='#ffffff')
        for skeleton in skeletons:
            color_changer: ColorChanger = ColorChanger(
                skeleton, left_color_picker, right_color_picker, center_color_picker)
            left_color_picker.observe(color_changer.update_left_objects, names='value')
            right_color_picker.observe(color_changer.update_right_objects, names='value')
            center_color_picker.observe(color_changer.update_center_objects, names='value')
            all_color_picker.observe(color_changer.update_all_objects, names='value')
        return VBox([left_color_picker, right_color_picker, center_color_picker, all_color_picker])

    def __get_default_left_color(self, skeletons: List[DrawableSkeleton]) -> str:
        if (len(skeletons) == 1):
            return self.__get_as_html_color(skeletons[0].get_left_objects()[0].color)
        return '#ffffff'

    def __get_default_right_color(self, skeletons: List[DrawableSkeleton]) -> str:
        if (len(skeletons) == 1):
            return self.__get_as_html_color(skeletons[0].get_right_objects()[0].color)
        return '#ffffff'

    def __get_default_center_color(self, skeletons: List[DrawableSkeleton]) -> str:
        if (len(skeletons) == 1):
            return self.__get_as_html_color(skeletons[0].get_center_objects()[0].color)
        return '#ffffff'

    @staticmethod
    def __get_as_html_color(color: int):
        return '{0:#0{1}x}'.format(color, 8).replace('0x', '#')


class MuPoTSVisualizer(SkeletonVisualizer):
    def __init__(self, size_scalar: float = 1.0):
        super().__init__(joint_set=MuPoTSJoints(), size_scalar=size_scalar)


class OpenPoseVisualizer(SkeletonVisualizer):
    def __init__(self, size_scalar: float = 1.0):
        super().__init__(joint_set=OpenPoseJoints(), size_scalar=size_scalar)


class CocoExVisualizer(SkeletonVisualizer):
    def __init__(self, size_scalar: float = 1.0):
        super().__init__(joint_set=CocoExJoints(), size_scalar=size_scalar)


class PanopticVisualizer(SkeletonVisualizer):
    def __init__(self, size_scalar: float = 1.0):
        super().__init__(joint_set=PanopticJoints(), size_scalar=size_scalar)


class Common14Visualizer(SkeletonVisualizer):
    def __init__(self, size_scalar: float = 1.0):
        super().__init__(joint_set=Common14Joints(), size_scalar=size_scalar)
